'''
import streamlit as st
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

st.set_page_config("Bodha AI by Skandan", layout="wide")
st.title("Bodha AI")

client =  InferenceClient(api_key=st.secrets["HF_TOKEN"])
col1, col2 = st.columns(2)

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
            label="⬇️ Download Image",
            data=img_buffer.getvalue(),
            file_name="generated.png",
            mime="image/png"
        )
    else:
        st.info("Generate content first")
'''
import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import io

st.set_page_config("Bodha AI by Skandan", layout="wide")
st.title("Bodha AI")

# HF Token is stored in Streamlit secrets
client = InferenceClient(api_key=st.secrets["HF_TOKEN"])

col1, col2 = st.columns(2)

st.image("bodhaai.jpeg", width=150, caption="Bodha AI")

with col1:
    inputprompt = st.text_input("Enter the Description")

    if st.button("Generate Content"):
        with st.spinner("Generating image..."):
            prompt = inputprompt.strip()

            # Call HF inference endpoint for SDXL
            response = client.post(
                model="stabilityai/stable-diffusion-xl-base-1.0",
                inputs=prompt,
                headers={"Accept": "image/png"}   # ensures raw image output
            )

            # Convert HTTPResponse → bytes
            img_bytes = response.read()

            # Convert bytes → PIL Image
            st.session_state.image = Image.open(io.BytesIO(img_bytes))

with col2:
    if "image" in st.session_state:
        st.image(st.session_state.image, width=400)

        # Prepare for download
        img_buffer = io.BytesIO()
        st.session_state.image.save(img_buffer, format="PNG")

        st.download_button(
            label="⬇️ Download Image",
            data=img_buffer.getvalue(),
            file_name="generated.png",
            mime="image/png"
        )
    else:
        st.info("Generate content first")
