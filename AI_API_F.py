
#API calls to AI

import requests


model_id="deepseek-ai/DeepSeek-R1"
API_URL ="https://api-inference.huggingface.com/models/deepseek-ai/DeepSeek-R1"
API_KEY="YOUR_API_KEY"
headers = {
"Authorization":f"Bearer{API_KEY}" ,
"x-use-cache": "true",
"Content-Type": "application/json"
}

#caching for efficiency in long prompt chains

prompt=" place your prompt here "

payload = {
    "inputs": f"{prompt}",
}

response = requests.get(API_URL, headers=headers, json=payload)

response2=response.text

print(response2)
