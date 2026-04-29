import streamlit as st
from components.bar_char import show_bar_chart
from components.confidence import show_confidence
from components.confidence_trend import show_confidence_trend

def render_right_panel(animal_names):
    top1, top2 = st.columns([3, 1])

    with top1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.header("Probabilities", divider="green")
        st.subheader("Class Probability", divider=False)

        show_bar_chart(animal_names, st.session_state.predictions)

        st.markdown('</div>', unsafe_allow_html=True)

    with top2:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        show_confidence(st.session_state.predictions)

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)

    show_confidence_trend(
        st.session_state.history_full,
        animal_names
    )

    st.markdown('</div>', unsafe_allow_html=True)