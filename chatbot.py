import gradio as gr
import requests

# Hugging Face API (free inference)
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
HEADERS = {"Authorization": "Bearer hf_your_api_key"}  # Get a free API key from HF

def chatbot_response(message):
    payload = {"inputs": message}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    try:
        return response.json()["generated_text"]
    except:
        return "Oops! The model is currently unavailable. Try again later."

# Gradio Interface
iface = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs="text",
    title="Simple AI Chatbot",
    description="Talk to a chatbot powered by a free Hugging Face model!",
)

iface.launch()