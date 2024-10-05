from flask import Flask, render_template, request, jsonify
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

app = Flask(__name__)

# Load the model and tokenizer
model_name = "t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

@app.route('/')
def home():
    return render_template('index.html')  # This should point to your HTML file

@app.route('/extract_skills', methods=['POST'])
def extract_skills():
    data = request.get_json()
    job_description = data.get('job_description', '')
    job_title = data.get('job_title', '')

    # Combine job title and description
    input_text = f"{job_title}: {job_description}"
    
    # Tokenize and generate skills
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True, padding="max_length", max_length=64)
    outputs = model.generate(inputs.input_ids)
    skills = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return jsonify({"skills": skills})

if __name__ == '__main__':
    app.run(debug=True)
