
import sys
from pathlib import Path
import streamlit as st
from transformers import pipeline
from PIL import Image

#### Image Generation ####
st.title("Background Remover")

# Load the model using transformers pipeline
model = pipeline("image-segmentation", model="mattmdjaga/segformer_b2_clothes")

# File uploader with the unique key from session state
uploaded_image = st.file_uploader("Choose a photo", type=["jpg", "jpeg", "png"])

if st.button("Remove Background"):
    with st.spinner('Removing Background...'):
        if uploaded_image is not None:
            pil_image = Image.open(uploaded_image)
            result = model(images=pil_image)

            # Background
            background = result[0]['mask']
            st.image(background, caption="Background")

            # Hair
            hair = result[1]['mask']
            st.image(hair, caption="Hair")
