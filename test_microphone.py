import speech_recognition as sr
import pyaudio

print("=" * 50)
print("MICROPHONE DIAGNOSTIC TOOL")
print("=" * 50)

# List all available microphones
print("\nAvailable Audio Devices:")
p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    if info['maxInputChannels'] > 0:
        print(f"  [{i}] {info['name']}")
        print(f"      Sample Rate: {int(info['defaultSampleRate'])}")
        print(f"      Input Channels: {info['maxInputChannels']}")
p.terminate()

print("\n" + "=" * 50)
print("MICROPHONE TEST")
print("=" * 50)

# Test microphone
r = sr.Recognizer()
try:
    print("\nTesting default microphone...")
    with sr.Microphone() as source:
        print(f"✓ Microphone detected!")
        print(f"  Energy threshold: {r.energy_threshold}")
        print("\nAdjusting for ambient noise... (be quiet)")
        r.adjust_for_ambient_noise(source, duration=2)
        print(f"  New energy threshold: {r.energy_threshold}")
        print("\n🎤 Say something now!")
        audio = r.listen(source, timeout=10, phrase_time_limit=5)
        print("✓ Audio captured!")
        
        print("\nRecognizing speech...")
        text = r.recognize_google(audio)
        print(f"✓ You said: '{text}'")
        print("\n✅ Microphone is working correctly!")
        
except sr.WaitTimeoutError:
    print("\n❌ No speech detected. Possible issues:")
    print("   - Microphone is muted")
    print("   - Microphone input level is too low")
    print("   - Wrong microphone is selected as default")
    print("   - Microphone permissions not granted")
    
except sr.UnknownValueError:
    print("\n⚠ Audio captured but speech not recognized")
    print("   Try speaking more clearly or louder")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nPossible issues:")
    print("   - No microphone connected")
    print("   - Microphone permissions not granted")
    print("   - Microphone is being used by another application")

print("\n" + "=" * 50)
