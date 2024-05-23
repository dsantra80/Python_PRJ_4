from flask import Blueprint, render_template, request, jsonify
from transformers import pipeline
import os

main = Blueprint('main', __name__)

# Load the Hugging Face model
model_name = "Llama-3-8B-Instruct-Gradient-1048k"
token = os.getenv("HUGGINGFACE_TOKEN")
model = pipeline('text-generation', model=model_name, use_auth_token=token)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    response = model(prompt, max_length=50, num_return_sequences=1)
    generated_text = response[0]['generated_text']
    return jsonify({'generated_text': generated_text})
