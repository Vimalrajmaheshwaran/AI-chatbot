from flask import Flask, render_template, request, jsonify
from google import genai
import os

app = Flask(__name__)

# --- CONFIGURATION ---
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_API_KEY = "Enter your key here" # User must provide their own key
# ---------------------

client = genai.Client(api_key=GOOGLE_API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
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
