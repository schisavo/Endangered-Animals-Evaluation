import streamlit as st
from .model_status import show_model_status
from .uploader import image_uploader
from .prediction_result import handle_prediction

def render_left_panel(model, model_status, animal_names):
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.header("AI Image Clasification Model", divider="green")

        show_model_status(model_status)

        st.image(
            "https://cdn-icons-png.flaticon.com/512/4712/4712027.png",
            width=100
        )

        st.markdown("""
            Analyze an image of the 11 :red[threatened] :green[species] and identify 
            which class it belongs to with :blue[78% accuracy].
            🐘 🐆 🐒 🦁 🦧 🐼 🦏  
        """)

        uploaded_file, image = image_uploader(model)

        if model and image:
            handle_prediction(model, image, animal_names)

        st.markdown('</div>', unsafe_allow_html=True)