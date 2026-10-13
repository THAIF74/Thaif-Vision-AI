
import base64
import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(
    page_title="Thaif Vision AI",
    page_icon="👁️",
    layout="wide"
)

st.title("👁️ Thaif Vision AI")
st.write("Upload an image and ask AI questions about it.")

api_key = os.getenv("NVIDIA_API_KEY")

if not api_key or api_key == "your_actual_key_here":
    st.error(
        "NVIDIA API key not found. Add your key to the .env file "
        "and restart the app."
    )
    st.stop()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key
)

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png", "webp"]
)

question = st.text_area(
    "What would you like to know about the image?",
    value="Describe this image in simple detail.",
    height=100
)

if uploaded_file:
    st.image(
    uploaded_file,
    caption="Uploaded image",
    width="stretch"
)

if st.button("Analyze Image", type="primary"):
    if uploaded_file is None:
        st.warning("Please upload an image first.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            image_bytes = uploaded_file.getvalue()
            encoded_image = base64.b64encode(
                image_bytes
            ).decode("utf-8")

            mime_type = uploaded_file.type

            with st.spinner("AI is analyzing your image..."):
                response = client.chat.completions.create(
                    model="meta/llama-3.2-11b-vision-instruct",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": question
                                },
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": (
                                            f"data:{mime_type};base64,"
                                            f"{encoded_image}"
                                        )
                                    }
                                }
                            ]
                        }
                    ],
                    max_tokens=1000,
                    temperature=0.2
                )

            answer = response.choices[0].message.content

            st.subheader("AI Analysis")
            st.write(answer or "The model returned an empty response.")

        except Exception as error:
            st.error("Image analysis failed.")
            st.code(str(error))

st.divider()
st.caption("Thaif Vision AI | Python • Streamlit • NVIDIA AI")
