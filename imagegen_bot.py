import streamlit as st
from groq import Groq

st.set_page_config("Bodha AI by Skandan", layout="wide")
st.title("Bodha AI")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
col1, col2 = st.columns(2)

st.image("bodhaai.jpeg", width=150, caption="Bodha AI")


with col1:
    product = st.text_input("Product")
    audience = st.text_input("Audience")

    if st.button("Generate Content"):
        prompt = f"Write marketing content for {product} targeting {audience}."
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        st.session_state.text = response.choices[0].message.content

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


