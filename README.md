# AI Voice Assistant with Ollama

A fully-featured AI voice assistant that listens to your voice commands, processes them, and responds with intelligent answers using speech. This system combines speech recognition, local AI processing with Ollama, and text-to-speech for a complete hands-free experience.

## ✨ Features

- 🎤 **Voice Recognition** - Listens and understands your speech
- 🤖 **AI Responses** - Powered by Ollama (free, local AI)
- 🔊 **Text-to-Speech** - Speaks responses back to you
- ⚡ **Offline Operations** - Many features work without internet
- 💰 **Completely Free** - No API costs, runs entirely on your computer
- 🔒 **Private** - All conversations stay on your device

### Offline Capabilities

The assistant can handle these without internet or AI:
- 📅 Date and time queries
- 🧮 Math calculations (addition, subtraction, multiplication, division)
- 🌐 Opening websites (YouTube, Google, Facebook, Twitter, Instagram, Reddit, Amazon)
- 🔍 Web searches
- 👋 Greetings and common conversations
- 😄 Jokes
- ❓ Help and introduction

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [Commands](#commands)
- [File Structure](#file-structure)
- [Troubleshooting](#troubleshooting)

## Requirements

**System Requirements:**
- Windows 10/11
- Python 3.12 (Python 3.14 has compatibility issues)
- Microphone
- 2GB+ free disk space (for Ollama model)

**Python Libraries:**
- `speech_recognition` - Voice recognition
- `gTTS` - Google Text-to-Speech
- `playsound` - Audio playback
- `pyaudio` - Audio input
- `pygame` - Audio support
- `ollama` - Local AI model
- `os`, `datetime`, `webbrowser`, `re` (built-in)

## Installation

### Step 1: Set Up Python Environment

**Important:** Use Python 3.12, not 3.14!

```powershell
# Check if Python 3.12 is available
py -3.12 --version

# Create virtual environment with Python 3.12
py -3.12 -m venv myenv

# Activate the virtual environment
.\myenv\Scripts\Activate.ps1
```

### Step 2: Install Python Packages

```powershell
pip install SpeechRecognition gTTS playsound==1.2.2 pyaudio pygame ollama
```

### Step 3: Install Ollama

**Option A: Using winget**
```powershell
winget install Ollama.Ollama
```

**Option B: Manual Download**
Download from: https://ollama.ai/download/windows

### Step 4: Download AI Model

**After installing Ollama, open a NEW PowerShell window:**

```powershell
# Download the small, fast model (recommended for starting)
ollama pull llama3.2:1b
```

**Alternative Models:**
- `llama3.2:3b` - Better quality (2GB)
- `llama3.1:8b` - Best quality (4.7GB, slower)

To use a different model, set the environment variable:

```powershell
$env:OLLAMA_MODEL = "llama3.2:3b"
```

## Setup

1. **Clone or download this repository**
   ```powershell
   cd C:\Users\YourName\Desktop
   # Extract or clone the AI-Speaker-main folder
   ```

2. **Navigate to the project folder**
   ```powershell
   cd AI-Speaker-main
   ```

3. **Activate virtual environment**
   ```powershell
   .\myenv\Scripts\Activate.ps1
   ```

4. **Verify Ollama is running**
   ```powershell
   ollama --version
   ollama list  # Should show at least one model after you pull it
   ```

## Usage

1. **Ensure your microphone is connected and working**

2. **Run the AI assistant:**
   ```powershell
   python test_AI.py
   ```

3. **Wait for the prompt:**
   ```
   AI Voice Assistant started! Say 'close' to exit.
   Listening...
   ```

4. **Speak your command clearly**

5. **The AI will respond with voice output**

### Quick self-test (recommended)

To verify the code works without using your microphone or playing audio:

```powershell
python test_AI.py --self-test --no-tts
```

### Example Interactions

**Date/Time:**
- "What time is it?"
- "What's the date today?"
- "Tell me the current date and time"

**Calculations:**
- "Calculate 25 plus 17"
- "What's 100 divided by 4"
- "45 times 3"

**Open Websites:**
- "Open YouTube"
- "Open Google"
- "Open Reddit"

**Web Search:**
- "Search for Python tutorials"
- "Look up best pizza near me"

**General Questions (uses AI):**
- "What is Python?"
- "Tell me about the solar system"
- "How do I make pasta?"

**Exit:**
- "Close"
- "Exit"
- "Goodbye"
- "Quit"

## Commands

The assistant recognizes multiple variations of commands:

### Time & Date
- "what time is it", "tell me the time", "current time", "what's the date"

### Math
- "calculate 5 plus 3", "10 times 2", "divide 100 by 5"

### Web Actions
- "open [youtube/google/facebook/twitter/instagram/reddit/amazon]"
- "search for [anything]", "google search [anything]"

### Conversational
- "hello", "hi", "how are you", "thank you", "tell me a joke"
- "what's your name", "who are you", "what can you do"

### Exit
- "close", "exit", "quit", "goodbye", "bye", "shut down"
- "stop listening", "close program", "exit program"

## Configuration

You can tune behavior using environment variables (PowerShell examples):

- **Choose the Ollama model**
   ```powershell
   $env:OLLAMA_MODEL = "llama3.2:1b"
   ```
- **Point to a different Ollama host** (defaults to `http://127.0.0.1:11434`)
   ```powershell
   $env:OLLAMA_HOST = "http://127.0.0.1:11434"
   ```
- **Set the Ollama request timeout** (seconds; default is `20`)
   ```powershell
   $env:OLLAMA_TIMEOUT_SECONDS = "30"
   ```
- **Disable text-to-speech**
   ```powershell
   $env:AI_SPEAKER_TTS = "0"
   ```

## File Structure

```
AI-Speaker-main/
│
├── test_AI.py              # Main AI assistant script
├── test_microphone.py      # Microphone diagnostic tool
├── README.md               # This file
├── OLLAMA_SETUP.md        # Detailed Ollama setup guide
├── SETUP_API.md           # Old OpenAI setup (deprecated / not used)
│
└── myenv/                  # Virtual environment (Python 3.12)
    ├── Scripts/
    │   ├── python.exe
    │   ├── activate
    │   └── Activate.ps1
    └── Lib/
        └── site-packages/  # Installed packages
```

## Troubleshooting

### Microphone Issues

**Problem:** "No speech detected - timeout"

**Solutions:**
1. Run the diagnostic tool:
   ```powershell
   python test_microphone.py
   ```
2. Check Windows microphone permissions (Settings → Privacy → Microphone)
3. Increase microphone volume in Windows sound settings
4. Try speaking louder or closer to the microphone
5. Ensure no other application is using the microphone

### Ollama Issues

**Problem:** "Error: Ollama not found" or connection errors

**Solutions:**
1. Verify Ollama is installed:
   ```powershell
   ollama --version
   ```
   If you get "ollama is not recognized", Ollama isn't installed yet or your terminal needs to be restarted after installation.
2. Check if model is downloaded:
   ```powershell
   ollama list
   ```
3. Pull the model if missing:
   ```powershell
   ollama pull llama3.2:1b
   ```
4. Restart PowerShell after installing Ollama
5. Make sure Ollama service is running (it auto-starts with Windows)

### Python Version Issues

**Problem:** "ModuleNotFoundError: No module named 'aifc'"

**Solution:** You're using Python 3.13+ which removed the `aifc` module. Use Python 3.12:
```powershell
# Remove old environment
Remove-Item -Recurse -Force myenv

# Create new one with Python 3.12
py -3.12 -m venv myenv
.\myenv\Scripts\Activate.ps1

# Reinstall packages
pip install SpeechRecognition gTTS playsound==1.2.2 pyaudio pygame ollama
```

### Package Installation Issues

**Problem:** Can't install PyAudio or other packages

**Solutions:**
1. Make sure you're using Python 3.12
2. Try installing packages one by one:
   ```powershell
   pip install SpeechRecognition
   pip install gTTS
   pip install playsound==1.2.2
   pip install pyaudio
   pip install pygame
   pip install ollama
   ```

### Speech Recognition Issues

**Problem:** Recognition fails or is inaccurate

**Solutions:**
1. Speak more clearly and at moderate speed
2. Reduce background noise
3. Adjust the listen timeout in `record()` inside `test_AI.py`:
   ```python
   audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
   ```

### Testing / No-audio mode

If you want to validate logic without playing audio:

```powershell
python test_AI.py --no-tts
```

## Technical Details

### How It Works

1. **Microphone Capture** - PyAudio captures audio from your microphone
2. **Noise Adjustment** - The system adjusts for ambient noise
3. **Speech Recognition** - Google's speech recognition API converts audio to text
4. **Intent Detection** - The system checks if it can handle the query offline
5. **AI Processing** - If needed, Ollama processes the query with a local AI model
6. **Response Generation** - A response is generated (offline or via AI)
7. **Text-to-Speech** - gTTS converts the response to speech
8. **Audio Playback** - The response is played through your speakers

### Privacy & Security

- ✅ All AI processing happens locally on your computer
- ✅ No data is sent to external servers (except Google's speech recognition)
- ✅ Conversations are not stored permanently
- ✅ Temporary files are deleted after use
- ✅ No API keys or account required

## Model Options

### Speed vs Quality Trade-off

| Model | Size | Speed | Quality | Recommendation |
|-------|------|-------|---------|----------------|
| llama3.2:1b | 1.3GB | ⚡⚡⚡ Fast | ⭐⭐ Basic | Good for quick responses |
| llama3.2:3b | 2GB | ⚡⚡ Medium | ⭐⭐⭐ Good | **Recommended** |
| llama3.1:8b | 4.7GB | ⚡ Slower | ⭐⭐⭐⭐ Excellent | Best for complex questions |

To switch models:
1. Download the new model: `ollama pull llama3.2:3b`
2. Set the model for the app:
   ```powershell
   $env:OLLAMA_MODEL = "llama3.2:3b"
   ```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available for educational purposes.

This project is licensed under the MIT License. See the `LICENSE` file for more details.

