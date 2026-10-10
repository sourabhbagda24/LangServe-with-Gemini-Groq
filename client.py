import requests

BASE_URL = "http://localhost:8000"

def fetch_llm(model, kind, topic):
    url = f"{BASE_URL}/{model}/{kind}/invoke"
    try:
        response = requests.post(url, json={"input": {"topic": topic}})
        if response.status_code == 200:
            data = response.json()
            print(f"\n{model.capitalize()} {kind} Response:\n{data['output']['content']}")
        else:
            print(f"Error {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Could not connect to {model} API.\n{e}")

fetch_llm("gemini", "tech", "What is Python?")
fetch_llm("groq", "nontech", "What is 2+2*3 ?")