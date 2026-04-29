import streamlit as st
from services.model import get_model

def load_model_status():
    model = None
    status = "error"
    message = ""

    try:
        model = get_model()
        status = "success"
        message = "Model loaded"
    except Exception as e:
        message = str(e)

    return model, status, message


def show_model_status(status):
    if status == "success":
        st.badge("Model Ready", icon=":material/check:", color="green")
    else:
        st.badge("Model Missing", icon=":material/error:", color="red")
        st.info("👉 Ejecuta: python scripts/train.py --output cnn_model.keras")