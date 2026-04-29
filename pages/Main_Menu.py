import streamlit as st
from state.session import init_session
from components.model_status import load_model_status
from components.left_panel import render_left_panel
from components.right_panel import render_right_panel

animal_names = [
    "African Elephant", "Amur Leopard", "Arctic Fox", "Cheetahs", "Chimpanzee", 
    "Jaguars", "Lion", "Orangutan", "Panda", "Panthers", "Rhino"
]

# INIT
model, model_status, _ = load_model_status()
init_session(animal_names)

# HEADER
st.title("🌿 Endangered is :green[Animals] Evaluation")

# LAYOUT
col1, col2 = st.columns([2, 3])

with col1:
    render_left_panel(model, model_status, animal_names)

with col2:
    render_right_panel(animal_names)