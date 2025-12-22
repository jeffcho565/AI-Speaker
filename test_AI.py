import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import datetime

import webbrowser
import re
import ollama
import random
from typing import Callable, cast
import argparse

DEFAULT_OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
OLLAMA_TIMEOUT_SECONDS = float(os.getenv("OLLAMA_TIMEOUT_SECONDS", "20"))

ENABLE_TTS = os.getenv("AI_SPEAKER_TTS", "1") not in {"0", "false", "False", "no", "NO"}

try:
    OLLAMA_CLIENT = ollama.Client(host=OLLAMA_HOST, timeout=OLLAMA_TIMEOUT_SECONDS)
except Exception:
    OLLAMA_CLIENT = None
_OLLAMA_READY_MODELS: set[str] = set()

# Pre-compile regex for faster matching
NUMBER_PATTERN = re.compile(r'\d+\.?\d*')
WORD_PATTERN = re.compile(r"[a-zA-Z']+")

# Cache recognizer to avoid recreating it
recognizer = sr.Recognizer()
recognizer.energy_threshold = 4000  # Higher = less sensitive to noise
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8  # Shorter pause detection

# Pre-defined responses for faster access
JOKES = [
    "Why don't programmers like nature? It has too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "What do you call a computer that sings? A Dell!",
    "Why was the JavaScript developer sad? Because he didn't know how to null his feelings!"
]


def _ollama_is_available() -> bool:
    """Return True if the Ollama local server is reachable."""
    try:
        # Will raise if the Ollama service isn't running/reachable.
        if OLLAMA_CLIENT is not None:
            OLLAMA_CLIENT.list()
        else:
            ollama.list()
        return True
    except Exception:
        return False


def _ensure_ollama_model(model: str) -> tuple[bool, str | None]:
    """Ensure a given Ollama model is present locally; attempts to pull if missing."""
    if model in _OLLAMA_READY_MODELS:
        return True, None

    if not _ollama_is_available():
        return (
            False,
            (
                "Ollama isn't installed or running on this PC. "
                "Install it from ollama.ai, restart PowerShell, then run: "
                f"ollama pull {model}"
            ),
        )

    try:
        models = (OLLAMA_CLIENT.list() if OLLAMA_CLIENT is not None else ollama.list()).get("models", [])
        names = {m.get("name", "") for m in models}
        if model not in names:
            # Pull the model on-demand (first run).
            print(f"[AI]: Downloading model '{model}' (first run). This can take a few minutes...")
            if OLLAMA_CLIENT is not None:
                OLLAMA_CLIENT.pull(model)
            else:
                ollama.pull(model)
        _OLLAMA_READY_MODELS.add(model)
        return True, None
    except Exception as e:
        msg = str(e)
        # Common case: Ollama running but model missing
        if "status code: 404" in msg or "not found" in msg.lower():
            return (
                False,
                f"The Ollama model '{model}' isn't downloaded yet. Run: ollama pull {model}",
            )
        return (
            False,
            "I couldn't reach Ollama or download the model. "
            "Make sure Ollama is installed, then run: "
            f"ollama pull {model}",
        )

def speach(text):
    """Convert text to speech and play it"""
    if not ENABLE_TTS:
        return
    mp3_file = 'sample.mp3'
    tts_en = gTTS(text=text, lang='en', slow=False)
    tts_en.save(mp3_file)
    playsound(mp3_file)
    os.remove(mp3_file)
        

def record():
    """Record audio and convert to text - optimized version"""
    try:
        with sr.Microphone() as source:
            # Quick noise adjustment
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=8)
        
        # Pylance/Pyright sometimes can't see recognize_google (dynamic attribute). Cast for type-checking.
        recognize_google = cast(Callable[..., str], getattr(recognizer, "recognize_google"))
        text = recognize_google(audio, language='en-US')
        print(f"[User]: {text}")
        return text
    except sr.WaitTimeoutError:
        return ""
    except sr.UnknownValueError:
        print("Recognition Failed")
        return ""
    except sr.RequestError as e:
        print(f"Request Failed: {e}")
        return ""
        
def ai_answer(text):
    """Process user input and generate response - optimized"""
    text_lower = text.lower()
    response = None
    
    # Use sets for faster keyword lookup
    # 1. Date/Time queries (offline)
    if any(k in text_lower for k in ["what time", "tell me the time", "what's the time", 
                                       "what is the time", "current time", "what day is it", 
                                       "what is the date", "what's the date", "date and time"]):
        response = f"The date and time is: {datetime.datetime.now().strftime('%m/%d/%Y %I:%M %p')}"
    
    # 2. Math calculations (offline)
    elif any(w in text_lower for w in ["calculate", "plus", "minus", "times", "divided", "multiply", "add", "subtract"]):
        try:
            numbers = NUMBER_PATTERN.findall(text_lower)
            if len(numbers) >= 2:
                a, b = float(numbers[0]), float(numbers[1])
                if "plus" in text_lower or "add" in text_lower:
                    result = a + b
                elif "minus" in text_lower or "subtract" in text_lower:
                    result = a - b
                elif "times" in text_lower or "multiply" in text_lower:
                    result = a * b
                elif "divided" in text_lower and b != 0:
                    result = a / b
                else:
                    result = None
                if result is not None:
                    response = f"The answer is {result}"
        except:
            pass
    
    # 3. Opening websites (offline)
    elif "open" in text_lower:
        sites = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "facebook": "https://www.facebook.com",
            "twitter": "https://www.twitter.com",
            "instagram": "https://www.instagram.com",
            "reddit": "https://www.reddit.com",
            "amazon": "https://www.amazon.com"
        }
        for site, url in sites.items():
            if site in text_lower:
                webbrowser.open(url)
                response = f"Opening {site.capitalize()}"
                break
    
    # 4. Search queries (offline - opens browser)
    elif any(w in text_lower for w in ["search for", "google search", "look up", "find information"]):
        search_term = text_lower
        for phrase in ["search for", "google search", "look up", "find information about"]:
            search_term = search_term.replace(phrase, "")
        search_term = search_term.strip()
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
        response = f"Searching for {search_term}"
    
    # 5. Introduction/Help (offline)
    elif any(p in text_lower for p in ["who are you", "what are you", "what can you do", "help me", "what do you do"]):
        response = "I am your AI voice assistant. I can answer questions, do calculations, open websites, tell you the time, and much more!"
    
    # 6. Simple greetings (offline)
    elif any(g in text_lower for g in ["hello", "hi ", "hey ", "good morning", "good afternoon", "good evening"]):
        hour = datetime.datetime.now().hour
        if hour < 12:
            response = "Good morning! How can I help you?"
        elif hour < 18:
            response = "Good afternoon! How can I help you?"
        else:
            response = "Good evening! What can I do for you?"
    
    # 7. Common conversational questions (offline)
    elif any(p in text_lower for p in ["how are you", "how's it going", "what's up"]):
        response = "I'm doing great, thank you! How can I assist you?"
    
    elif any(p in text_lower for p in ["thank you", "thanks", "appreciate"]):
        response = "You're welcome!"
    
    elif any(p in text_lower for p in ["what's your name", "your name", "who made you"]):
        response = "I'm your AI voice assistant, created to help you with tasks and answer questions."
    
    elif any(p in text_lower for p in ["tell me a joke", "joke", "make me laugh", "something funny"]):
        response = random.choice(JOKES)
    
    elif "weather" in text_lower:
        response = "I don't have real-time weather data, but say 'search for weather' and I'll help you find it!"
    
    # If no offline handler matched, use Ollama
    if response is None:
        try:
            print("[AI]: Thinking...")
            model = DEFAULT_OLLAMA_MODEL
            ok, err = _ensure_ollama_model(model)
            if not ok:
                response = (
                    "I can answer basic commands offline, but my local AI model isn't ready. "
                    + (err or "Please install Ollama and download a model.")
                )
            else:
                result = (OLLAMA_CLIENT.chat if OLLAMA_CLIENT is not None else ollama.chat)(
                    model=model,
                    messages=[
                        {"role": "system", "content": "You are a helpful voice assistant. Keep responses very concise, under 40 words."},
                        {"role": "user", "content": text}
                    ],
                    options={
                        "temperature": 0.7,
                        "num_predict": 100,  # Limit response length for speed
                    }
                )
                response = result["message"]["content"]
        except Exception as e:
            print(f"[AI Error]: {e}")
            response = (
                "I'm having trouble using the local AI model. "
                f"If Ollama is installed, try: ollama pull {DEFAULT_OLLAMA_MODEL}"
            )
    
    # Speak the response
    print(f"[AI]: {response}")
    speach(response)
    return response


def self_test() -> int:
    """Non-interactive smoke test for offline logic + Ollama connectivity."""
    global ENABLE_TTS
    ENABLE_TTS = False

    tests = [
        "what time is it",
        "what's the date",
        "calculate 10 plus 5",
        "tell me a joke",
        "who are you",
        "how are you",
        "thanks",
    ]

    print("[SELF-TEST] Running offline tests...")
    for t in tests:
        r = ai_answer(t)
        if not isinstance(r, str) or not r.strip():
            print(f"[SELF-TEST] FAIL: empty response for: {t!r}")
            return 1

    print("[SELF-TEST] Offline handlers OK")

    if _ollama_is_available():
        print("[SELF-TEST] Ollama reachable. Model check will be attempted on first AI question.")
    else:
        print("[SELF-TEST] Ollama NOT reachable (this is OK if you haven't installed it yet).")

    print("[SELF-TEST] PASS")
    return 0
     
def main():
    """Main loop - optimized for speed"""
    print("AI Voice Assistant started! Say 'close' to exit.")
    
    # Exit phrases (keep this strict to avoid accidental exits like "stop your playing")
    close_phrases = {
        "close",
        "exit",
        "quit",
        "goodbye",
        "bye",
        "shutdown",
        "shut down",
        "terminate",
        "end",
        "stop listening",
        "close program",
        "exit program",
        "quit program",
    }
    close_first_word = {"close", "exit", "quit", "shutdown", "terminate"}
    
    while True:
        user_input = record()
        
        if not user_input:
            continue
            
        user_input_lower = user_input.lower()
        
        # Check for exit command (strict matching)
        cleaned = " ".join(WORD_PATTERN.findall(user_input_lower)).strip()
        tokens = cleaned.split()
        is_close = False
        if cleaned in close_phrases:
            is_close = True
        elif tokens and tokens[0] in close_first_word and len(tokens) <= 2:
            # e.g. "close" or "close please" or "exit now"
            is_close = True

        if is_close:
            print("[AI]: Goodbye")
            speach("Goodbye")
            break
            
        ai_answer(user_input)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--self-test", action="store_true", help="Run a quick non-interactive test and exit")
    parser.add_argument("--no-tts", action="store_true", help="Disable text-to-speech (useful for testing)")
    args = parser.parse_args()

    if args.no_tts:
        ENABLE_TTS = False

    if args.self_test:
        raise SystemExit(self_test())

    main()
