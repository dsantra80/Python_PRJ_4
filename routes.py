from flask import Blueprint, render_template, request, jsonify
import requests
import os

main = Blueprint('main', __name__)

# Hugging Face API configuration
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
token = os.getenv("HUGGINGFACE_TOKEN")
headers = {"Authorization": f"Bearer {token}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    output = query({"inputs": prompt})
    generated_text = output[0]['generated_text']
    return jsonify({'generated_text': generated_text})
