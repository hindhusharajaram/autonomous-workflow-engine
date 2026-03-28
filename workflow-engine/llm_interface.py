import json
from groq import Groq

try:
    from google.colab import userdata
    api_key = userdata.get('GROQ_API_KEY')
    client = Groq(api_key=api_key)
except Exception:
    client = None
    print("API Key Error: Ensure 'GROQ_API_KEY' is set")

def call_intelligence(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except:
        return {"decisions": []}
