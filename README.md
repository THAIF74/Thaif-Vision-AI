
# Thaif Vision AI

A Vision AI Assistant that analyzes uploaded images and answers
questions using a vision-capable NVIDIA AI model.

## Features

- Upload JPG, JPEG, PNG, and WebP images
- Ask questions about uploaded images
- Generate image descriptions and visual observations
- Interactive web interface built with Streamlit

## Technologies

- Python
- Streamlit
- NVIDIA API
- OpenAI-compatible Python SDK

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies using `pip install -r requirements.txt`.
3. Add your NVIDIA API key to a local `.env` file.
4. Run `streamlit run app.py`.

Never upload your `.env` file or expose your API key.
## Features

- Upload images in JPG, JPEG, PNG, and WebP formats.
- Ask natural-language questions about images.
- Receive AI-generated visual descriptions and answers.
- View conversation history during the active session.
- Clear the current conversation using New Chat.
- Run locally or deploy through Streamlit Community Cloud.

## Technology Stack

- Python
- Streamlit
- NVIDIA API
- Meta Llama 3.2 11B Vision Instruct
- OpenAI-compatible Python SDK
- python-dotenv
- Git and GitHub

## Documentation

Project documentation is available in the `docs/` folder:

- `project_synopsis.md` — project overview, objectives, and conclusion.
- `architecture.md` — system components and architecture.
- `workflow.md` — workflow and testing plan.
- `viva_questions.md` — viva preparation questions and answers.

## Security

Never commit your real API key to GitHub. Configure `NVIDIA_API_KEY` in your local `.env` file for local development and in Streamlit Community Cloud Secrets for deployment.

## Limitations

The application requires internet connectivity and access to the configured AI API. Responses may be inaccurate, and chat history is temporary rather than permanently stored.

## Future Enhancements

- Persistent conversation history.
- Image comparison and multi-image analysis.
- Improved error handling.
- Additional computer vision capabilities.

## Repository

GitHub: https://github.com/THAIF74/Thaif-Vision-AI
