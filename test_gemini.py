import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env
load_dotenv()

_api_key = os.environ.get("GEMINI_API_KEY")
if not _api_key:
    raise RuntimeError("GEMINI_API_KEY is not set. Add it to your .env file.")

client = genai.Client(api_key=_api_key)

models_to_test = [
    "gemini-2.5-flash", 
    "gemini-2.0-flash", 
    "gemini-1.5-flash", 
    "gemini-1.5-flash-8b",
]

for m in models_to_test:
    try:
        response = client.models.generate_content(
            model=m,
            contents="say hi",
        )
        print(f"SUCCESS with {m}: {response.text}")
    except Exception as e:
        print(f"FAILED with {m}: {str(e)}")
