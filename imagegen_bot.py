'''
import streamlit as st
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
from huggingface_hub import InferenceClient
import io

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
        st.session_state.image = response.choices[0].message.content

with col2:
    if "image" in st.session_state:
        st.image(st.session_state.image, width=400)

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

----------------------------------------------------------------
import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import io

st.set_page_config("Bodha AI by Skandan", layout="wide")
st.title("Bodha AI")

client = InferenceClient(
    "stabilityai/stable-diffusion-xl-base-1.0",
    token=st.secrets["HF_TOKEN"]
)

col1, col2 = st.columns(2)

st.image("bodhaai.jpeg", width=150, caption="Bodha AI")

with col1:
    inputprompt = st.text_input("Enter the Description")

    if st.button("Generate Content"):
        with st.spinner("Generating image..."):
            image = client.text_to_image(inputprompt)
            st.session_state.image = image

with col2:
    if "image" in st.session_state:
        st.image(st.session_state.image, width=400)

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
'''

import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import io

st.set_page_config("Bodha AI by Skandan", layout="wide")
st.title("Bodha AI")

client = InferenceClient(
    "runwayml/stable-diffusion-v1-5",
    token=st.secrets["HF_TOKEN"]
)

col1, col2 = st.columns(2)

st.image("bodhaai.jpeg", width=150, caption="Bodha AI")

with col1:
    inputprompt = st.text_input("Enter the Description")

    if st.button("Generate Content"):
        with st.spinner("Generating image..."):
            image = client.text_to_image(inputprompt)
            st.session_state.image = image

with col2:
    if "image" in st.session_state:
        st.image(st.session_state.image, width=400)

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
