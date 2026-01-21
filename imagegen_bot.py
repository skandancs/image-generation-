import streamlit as st
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

st.set_page_config("Bodha AI by Skandan", layout="wide")
st.title("Bodha AI")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
col1, col2 = st.columns(2)
cols = st.columns(3)  # 3-column grid

st.image("bodhaai.jpeg", width=150, caption="Bodha AI")


with col1:
    inputprompt = st.text_input("Enter the Description")

    if st.button("Generate Content"):
        prompt = f"Generate a image for {inputprompt}"
        response = client.chat.completions.create(
            model="runwayml/stable-diffusion-v1-5",
            messages=[{"role": "user", "content": prompt}]
        )
        st.session_state.text = response.choices[0].message.content

with col2:
    if "text" in st.session_state:
        content = st.text_area("Generated Content", st.session_state.text, height=300)

        st.download_button(
            label="⬇️ Download as TXT",
            data=content,
            file_name="marketing_copy.txt",
            mime="text/plain"
        )
    else:
        st.info("Generate content first")
