
import requests

url = "https://api.groq.com/openai/v1/chat/completions"
api_key = "YOUR_GROQ_API_KEY"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "llama3-70b-8192",  
    "messages": [{"role": "user", "content": "give me an interesting fact."}], # got them from docs
    "temperature": 0.7 #set lower for accuracy,set higher for creativity
}

response = requests.post(url, headers=headers, json=data)
print(response.json())