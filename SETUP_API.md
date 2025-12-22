# AI Speaker Setup - OpenAI API

## Get Your OpenAI API Key

1. Go to [https://platform.openai.com/signup](https://platform.openai.com/signup)
2. Create an account or sign in
3. Go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
4. Click "Create new secret key"
5. Copy your API key

## Setup Options

### Option 1: Environment Variable (Recommended)
Set the environment variable in PowerShell:
```powershell
$env:OPENAI_API_KEY="your-api-key-here"
```

### Option 2: Direct in Code
Open `test_AI.py` and replace this line:
```python
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"))
```
with:
```python
client = OpenAI(api_key="your-actual-api-key-here")
```

## Free Alternative: Use Ollama (Local AI)

If you don't want to pay for OpenAI, you can use Ollama to run AI models locally:

1. Install Ollama from [https://ollama.ai](https://ollama.ai)
2. Run: `ollama pull llama2`
3. I can modify the code to use Ollama instead

Let me know which option you prefer!

## Cost Information

- OpenAI GPT-3.5-turbo: ~$0.002 per conversation
- GPT-4: More expensive but better quality
- Ollama: Completely free but runs on your computer
