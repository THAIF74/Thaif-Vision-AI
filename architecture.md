# Thaif Vision AI — System Architecture

## 1. Overview

Thaif Vision AI is a web-based image understanding application. It accepts an image and a natural-language question from the user, sends the request to a vision-capable AI model through the NVIDIA API, and displays the generated response.

## 2. Architecture Diagram

```text
+---------------------------+
|           User            |
| Uploads Image and Question|
+-------------+-------------+
              |
              v
+---------------------------+
|     Streamlit Interface   |
| Image Upload and Chat UI  |
+-------------+-------------+
              |
              v
+---------------------------+
|     Python Application    |
| Input Handling and Image  |
| Encoding                  |
+-------------+-------------+
              |
              v
+---------------------------+
|         NVIDIA API        |
| Vision Model Request      |
+-------------+-------------+
              |
              v
+---------------------------+
| Meta Llama 3.2 11B Vision |
| Image Understanding       |
+-------------+-------------+
              |
              v
+---------------------------+
| AI Response and Chat UI   |
+---------------------------+
```

## 3. Main Components

### 3.1 User Interface
Streamlit provides the web interface for uploading images, entering questions, viewing answers, and clearing the current conversation.

### 3.2 Application Logic
Python handles user inputs, image encoding, API communication, response processing, and conversation history.

### 3.3 Image Processing
The uploaded image is encoded in Base64 format and included in the API request using a data URL.

### 3.4 AI Model
The application uses the Meta Llama 3.2 11B Vision Instruct model through NVIDIA's API to generate responses about uploaded images.

### 3.5 Conversation Management
Streamlit session state stores the text questions and answers during the active session. The New Chat feature clears this history.

### 3.6 Configuration and Deployment
The NVIDIA API key is configured locally using an environment file and on Streamlit Community Cloud using its Secrets facility. GitHub stores the application source code.

## 4. Data Flow

1. The user uploads a supported image.
2. The user enters a question.
3. The Python application encodes the image and prepares the request.
4. The application sends the question and image to the NVIDIA API.
5. The vision model processes the request.
6. The API returns the generated answer.
7. Streamlit displays the answer and updates the conversation history.

## 5. Security Considerations

- API keys must not be committed to the public repository.
- Local credentials should be excluded through `.gitignore`.
- Streamlit Community Cloud Secrets should be used for deployment credentials.
- API requests require internet connectivity.

## 6. Conclusion

The architecture separates the user interface, Python application logic, external AI service, and conversation management. This design makes the application easier to maintain and extend.
