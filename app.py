from flask import Flask, render_template, request, jsonify
from google import genai
import os

app = Flask(__name__)

# --- CONFIGURATION ---
# This is perfect for GitHub. It keeps your real key safe.
GOOGLE_API_KEY = "Enter your key here" 
# ---------------------

client = genai.Client(api_key=GOOGLE_API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_data = request.get_json()
        user_message = user_data.get('message')

        response = client.models.generate_content(
            model='gemini-flash-latest', 
            contents=user_message
        )
        
        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"response": f"System Error: {str(e)}"})