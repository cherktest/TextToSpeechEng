import streamlit as st
import requests
import base64

st.title("Преобразование английского текста в речь 💬 ")

inp_text = st.text_input("Введите свой текст здесь.....")

button = st.button(" Преобразование текста в речь 🦄")

if button:

    with st.spinner():

        response_json = requests.post("https://abidlabs-speak.hf.space/run/predict", json={
        "data": [
            inp_text,
        ]}).json()


        md = f"""
            <audio controls>
            <source src="{response_json['data'][0]}" type="audio/flac">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

