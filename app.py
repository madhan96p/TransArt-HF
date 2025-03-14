import os
import gradio as gr
import requests
import io
from PIL import Image
from groq import Groq

# API Keys
HF_IMAGE_MODEL = "stabilityai/stable-diffusion-2"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
API_TOKEN = os.getenv("HF_API_KEY")

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}


# Initialize Groq API client
groq_client = Groq(api_key=GROQ_API_KEY)

# Function: Tamil Audio → Tamil Text
def transcribe_audio(audio_file_path):
    try:
        with open(audio_file_path, "rb") as audio_file:
            transcription = groq_client.audio.transcriptions.create(
                file=("audio.wav", audio_file.read()), model="whisper-large-v3", language="ta"
            )
        return transcription.text
    except Exception as e:
        return f"Error: {e}"

# Function: Tamil Text → English Translation
def translate_tamil_to_english(tamil_text):
    try:
        response = groq_client.chat.completions.create(
        translated_text = gr.Textbox(label="Translated English Text", interactive=True, visible=False)

        generate_image_btn = gr.Button("Generate Image", visible=False)
        generated_image = gr.Image(label="Generated Image", visible=False)

        generate_text_btn = gr.Button("Generate Text", visible=False)
        generated_text = gr.Textbox(label="Generated Text", interactive=True, visible=False)

    # Button Actions
    def show_transcribed(audio_file):
        text = process_audio(audio_file)
        return gr.update(value=text, visible=True), gr.update(visible=True)

    def show_translated(tamil_text):
        text = translate_text(tamil_text)
        return gr.update(value=text, visible=True), gr.update(visible=True)

    def show_image(english_text):
        image = generate_image(english_text)
        return gr.update(value=image, visible=True), gr.update(visible=True)

    def show_generated_text(english_text):
        text = generate_text(english_text)
        return gr.update(value=text, visible=True)

    transcribe_btn.click(show_transcribed, inputs=audio_input, outputs=[transcribed_text, translate_btn])
    translate_btn.click(show_translated, inputs=transcribed_text, outputs=[translated_text, generate_image_btn])
    generate_image_btn.click(show_image, inputs=translated_text, outputs=[generated_image, generate_text_btn])
    generate_text_btn.click(show_generated_text, inputs=translated_text, outputs=generated_text)

app.launch(share=True)

