import streamlit as st
from PIL import Image

def image_uploader(model):
    uploaded_file = st.file_uploader(
        "Upload an image of an animal",
        type=["jpg", "jpeg", "png"],
        disabled=(model is None)
    )

    if model is None:
        st.warning("⚠️ Modelo no disponible")
        return None, None

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", width=400)
        return uploaded_file, image

    return None, None