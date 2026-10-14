
import os
import base64
from io import BytesIO

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from PIL import Image

load_dotenv()

MODEL = "meta/llama-3.2-11b-vision-instruct"
API_BASE_URL = "https://integrate.api.nvidia.com/v1"

st.set_page_config(
    page_title="Thaif Vision AI",
    page_icon="👁️",
    layout="wide",
)

def get_api_key():
    key = os.getenv("NVIDIA_API_KEY")
    try:
        key = st.secrets.get("NVIDIA_API_KEY", key)
    except Exception:
        pass
    return key

def get_client():
    api_key = get_api_key()
    if not api_key:
        raise ValueError(
            "NVIDIA API key not found. Add NVIDIA_API_KEY "
            "to Streamlit Secrets or your local .env file."
        )
    return OpenAI(
        base_url=API_BASE_URL,
        api_key=api_key,
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("👁️ Thaif Vision AI")
st.caption("An AI-powered assistant that understands your images.")

with st.sidebar:
    st.header("⚙️ Controls")
    st.write("**Vision model:** Llama 3.2 11B Vision")
    st.write("**Powered by:** NVIDIA AI")
    st.divider()

    if st.button("🗑️ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.caption("Your conversation history stays in this "
               "browser session and is not saved permanently.")

left, right = st.columns([1, 1.3], gap="large")

with left:
    st.subheader("📷 Upload an Image")
    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png", "webp"],
    )

    image_bytes = None
    if uploaded_file:
        image_bytes = uploaded_file.getvalue()
        try:
            image = Image.open(BytesIO(image_bytes))
            st.image(image, caption=uploaded_file.name,
                     use_container_width=True)
        except Exception:
            st.error("Unable to read this image. Try another file.")
            image_bytes = None

    st.info(
        "Tip: Upload a clear image and ask a specific question "
        "for a more useful answer."
    )

with right:
    st.subheader("💬 Conversation")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.text_area(
        "Ask a question about your image",
        placeholder="Describe this image, identify objects, "
                    "or ask what is happening...",
        height=100,
        key="question_input",
    )

    analyze = st.button(
        "🔍 Analyze Image",
        type="primary",
        use_container_width=True,
        disabled=not image_bytes or not question.strip(),
    )

    if analyze:
        try:
            client = get_client()

            encoded_image = base64.b64encode(
                image_bytes
            ).decode("utf-8")

            mime_type = uploaded_file.type or "image/jpeg"
            data_url = (
                f"data:{mime_type};base64,{encoded_image}"
            )

            api_messages = [
                {
                    "role": "system",
                    "content": (
                        "You are Thaif Vision AI, a helpful image "
                        "understanding assistant. Answer clearly "
                        "and only claim visual details you can "
                        "reasonably identify."
                    ),
                }
            ]

            # Include previous text conversation for context.
            api_messages.extend(st.session_state.messages)

            api_messages.append({
                "role": "user",
                "content": [
                    {"type": "text", "text": question.strip()},
                    {
                        "type": "image_url",
                        "image_url": {"url": data_url},
                    },
                ],
            })

            with st.spinner("🧠 Analyzing your image..."):
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=api_messages,
                    max_tokens=700,
                    temperature=0.2,
                )

            answer = response.choices[0].message.content

            st.session_state.messages.append({
                "role": "user",
                "content": question.strip(),
            })
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer or "No answer was returned.",
            })

            st.rerun()

        except Exception as error:
            st.error(f"Analysis failed: {error}")

st.divider()
st.caption("Thaif Vision AI • Python • Streamlit • NVIDIA AI")
