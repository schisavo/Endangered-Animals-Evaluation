import numpy as np
import streamlit as st
from services.img_preprocessing import preprocess_image
from services.model import predict

def handle_prediction(model, image, animal_names):
    evaluate = st.button("Evaluate", disabled=(image is None))

    if not evaluate:
        return

    try:
        img_array = preprocess_image(image)

        with st.spinner("🧠 Analyzing image with AI..."):
            preds = predict(model, img_array)

        st.session_state.predictions = preds

        if "history_full" not in st.session_state:
            st.session_state.history_full = []

        st.session_state.history_full.append(preds)

        label = np.argmax(preds)
        animal = animal_names[label]

        st.success(f"✅ Predicted: {animal}")

        # Progress UX
        progress = st.progress(0)
        for i in range(100):
            progress.progress(i + 1)

    except Exception as e:
        st.error(f"❌ Error: {e}")