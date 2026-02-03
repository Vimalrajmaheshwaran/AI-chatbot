from flask import Flask, render_template, request, jsonify
from google import genai
import os

app = Flask(__name__)

# --- CONFIGURATION ---
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_API_KEY = "AIzaSyCGrr4F8amrqeIJsnm6fTVSw2SPoZeAIMk" # User must provide their own key
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
