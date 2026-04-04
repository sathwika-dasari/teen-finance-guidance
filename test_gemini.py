from google import genai

client = genai.Client(api_key="Your Api key")

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
