# Ollama Setup Instructions

## Step 1: Install Ollama

Download and install Ollama from: https://ollama.ai/download/windows

Or run this command:
```powershell
winget install Ollama.Ollama
```

## Step 2: Install the AI Model

After Ollama is installed, open a new PowerShell window and run:
```powershell
ollama pull llama3.2:1b
```

This downloads a small, fast AI model (about 1.3GB).

## Step 3: Test Ollama

Verify it's working:
```powershell
ollama run llama3.2:1b "Hello, how are you?"
```

## Step 4: Run Your AI Speaker

Now run your AI speaker:
```powershell
python test_AI.py
```

### Quick self-test (recommended)

This tests the offline features without using your microphone or playing audio:

```powershell
python test_AI.py --self-test --no-tts
```

## Model Options

- **llama3.2:1b** (Current) - Fastest, 1.3GB - Good for basic questions
- **llama3.2:3b** - Better quality, 2GB - Recommended upgrade
- **llama3.1:8b** - Best quality, 4.7GB - Slower but smarter

To switch models, set an environment variable:

```powershell
$env:OLLAMA_MODEL = "llama3.2:3b"
```

Then (if needed) download it:

```powershell
ollama pull llama3.2:3b
```

## Optional configuration

- Change Ollama host (default `http://127.0.0.1:11434`):
	```powershell
	$env:OLLAMA_HOST = "http://127.0.0.1:11434"
	```

- Increase Ollama request timeout (seconds; default `20`):
	```powershell
	$env:OLLAMA_TIMEOUT_SECONDS = "30"
	```

- Disable text-to-speech:
	```powershell
	$env:AI_SPEAKER_TTS = "0"
	```

## Troubleshooting

If you get an error:
1. Make sure Ollama is installed
2. Make sure you ran `ollama pull llama3.2:1b`
3. Restart your terminal/PowerShell (new window) after installing Ollama so the `ollama` command is available
4. Check if Ollama service is running: `ollama serve`

### Stuck on "[AI]: Thinking..."

This usually means the model is still downloading, or the Ollama service is busy.

1. Pre-download the model:
	```powershell
	ollama pull llama3.2:1b
	```
2. Confirm Ollama is reachable:
	```powershell
	ollama list
	```
3. Increase the timeout (optional):
	```powershell
	$env:OLLAMA_TIMEOUT_SECONDS = "30"
	```

### "ollama" is not recognized

That means Ollama isn't installed yet, or you need to open a **new** PowerShell/Terminal window after installation.

## Benefits

✅ Completely FREE - no API costs
✅ Works OFFLINE - no internet needed after download
✅ Private - your conversations stay on your computer
✅ Fast responses - runs locally on your machine
