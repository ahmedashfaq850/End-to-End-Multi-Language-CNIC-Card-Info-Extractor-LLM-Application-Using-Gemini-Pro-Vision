from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

my_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=my_api_key)
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def convert_image_into_bytes(uploaded_file):
    if upload_file is not None:
        bytes_data = uploaded_file.getvalue()
        
        image_parts = [
            {
                "mime_type": upload_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("File not found")


# Now streamlit code
st.set_page_config(page_title='Multi Language CNIC Card Extractor App')
st.header('Multi Language CNIC Card Info Extractor LLM App using Google Gemini')

input = st.text_input("Input Prompt: ", key="input")
upload_file = st.file_uploader("Choose and image tp upload the invoice", type=['jpg', 'png', 'jpeg'])
image = ""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
submit = st.button("Ask about Invoice")

### Now generate an input prompt to tell the llm model how to behave and what to do adn set limitations
input_prompt = """
You are as an expert in cnic card info extraction and you have been given an cnic card to extract the information from it.
You dont have to go beyond the cnic card and extract the information from the cnic card.
if anyone ask you the question out of the cnic, you can say that you are not able to answer the question.
you are only designed to extract the information from the cnic card. and you can only answer the questions related to the cnic card.
if the uploaded file is not an id card or cnic card, you can say that the uploaded file is not an id card or cnic card.
"""

if input and image and submit:
    image_data = convert_image_into_bytes(upload_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is")
    st.write(response)