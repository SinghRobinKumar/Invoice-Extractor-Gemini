from dotenv import load_dotenv
import base64

# Make sure to import this otherwise the env is not loaded
load_dotenv()

from google import genai
import os
import streamlit as st
from PIL import Image

# Configure Google AI
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=GOOGLE_API_KEY)


# Load Gemini Vision and get response
def get_gemini_response(input, image):
    # used gemini flash instead of google vision which was depreciated
    model = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[{"text": input}, {"inline_data": image[0]}],
    )
    return model.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]

        return image_parts

    else:
        raise FileNotFoundError("No file uploaded")


# Streamlit Setup

st.set_page_config(page_title="Invoice Extractor")

st.header("Gemini App")

input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader(
    "Choose a image...", type=["jpg", "jpeg", "png", "pdf", "webp"]
)
image = ""

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        # Show PDF preview using Streamlit's iframe-based viewer
        st.subheader("PDF Preview:")
        base64_pdf = base64.b64encode(uploaded_file.read()).decode("utf-8")
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    else:
        # Assume it's an image and show it
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

submit = st.button("Tell me about the invoice")


input_prompt = f"""
You are an expert in understanding invoices. You will receive the input images as invoices and you will have to answer the questions based on the input image.

Prompt:
{input}
"""

# Submit clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data)

    st.subheader("The response is")
    st.write(response)
