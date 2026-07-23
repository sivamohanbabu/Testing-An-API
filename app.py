import os 

from google import genai

API_KEY = ""

client = genai.Client(api_key=API_KEY)

try: 
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents="say welcome message!"
    )
    print("API working Sucessfully")
    print(response.text)
except Exception as e:
    print("API Error!")
    print(e)
