import requests
import json

API_KEY = "AIzaSyDBJkGUIhXMEgftO-Somji_yPtXi9WarmM"  # your real key
API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-pro:generateContent?key={API_KEY}"

def generate_gemini_response(prompt):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    print("📤 Sending request to Gemini API...")
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    print("📥 Response received!")

    print("🔍 Raw Response Text:", response.text)  # Add this line for debugging

    if response.status_code == 200:
        try:
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        except Exception as e:
            return f"✅ API responded but parsing failed: {e}\nFull JSON: {response.json()}"
    else:
        return f"❌ Error {response.status_code}: {response.text}"
