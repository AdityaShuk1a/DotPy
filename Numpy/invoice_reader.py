import pytesseract
from PIL import Image
import os
import openai
import google.generativeai as genai

# Set your OpenAI API key (ensure the environment variable is set)
"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""



genai.configure(api_key=os.environ[""])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
 
)

chat_session = model.start_chat(
  history=[]
)

response = chat_session.send_message("hello brother kese ho")

print(response.text)

# Tesseract setup for OCR (Optical Character Recognition)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# def extract_text_from_image(image_path):
#     """
#     Extracts text from an image using Tesseract.
#     """
#     try:
#         img = Image.open(image_path)
#         text = pytesseract.image_to_string(img)
#         print(text)
#     except FileNotFoundError:
#         print(f"File {image_path} not found.")

# def process_invoice(file_path):
#     """
#     Main function to process the invoice file.
#     """
#     ext = os.path.splitext(file_path)[1].lower()
#     if ext in ['.png', '.jpg', '.jpeg']:
#         text = extract_text_from_image(file_path)
#     else:
#         return {"status": 400, "response": "Unsupported file format"}

# # Example: process an image file (replace with actual file path)
# file_path = 'blue2.jpg' 
# process_invoice(file_path)
