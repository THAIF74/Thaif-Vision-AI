# Thaif Vision AI — Viva Questions and Answers

## Basic Questions

### 1. What is Thaif Vision AI?
It is a web application that accepts images and questions and uses a vision-capable AI model to generate answers.

### 2. What is the main objective?
The objective is to make image understanding accessible through a simple interactive interface.

### 3. Which programming language is used?
Python.

### 4. Which framework is used for the interface?
Streamlit, a Python framework for creating interactive web applications.

### 5. Which AI model is used?
Meta Llama 3.2 11B Vision Instruct, accessed through the NVIDIA API.

## Technical Questions

### 6. What is computer vision?
Computer vision is a field of artificial intelligence that enables computers to interpret and analyze visual information such as images and videos.

### 7. What is a vision-language model?
It is a model that can process visual inputs and natural-language instructions to produce text responses.

### 8. What is an API?
An Application Programming Interface allows different software components to communicate through defined requests and responses.

### 9. Why is the NVIDIA API used?
It provides access to the configured AI model so the application can request image understanding without hosting the model locally.

### 10. What is Base64 encoding?
Base64 represents binary data as text characters. This project uses it to include image data in an API request.

### 11. What is the purpose of the OpenAI-compatible Python SDK?
It provides a client interface for sending chat-completion requests to a compatible API endpoint.

### 12. What is Streamlit session state?
It is a mechanism for retaining application data across Streamlit reruns within a user session.

### 13. How does chat history work?
The application stores text questions and answers in session state and displays them in the conversation interface.

### 14. Does the application permanently save conversations?
No. The current implementation keeps the conversation temporarily and does not use a permanent database.

### 15. What is the purpose of the New Chat button?
It clears the current conversation history and lets the user start a fresh interaction.

## Security and Deployment

### 16. What is an environment variable?
It is a configuration value supplied to a running application without embedding it directly in the source code.

### 17. Why should API keys not be uploaded to GitHub?
Exposed credentials could be misused by others, potentially leading to unauthorized API requests or charges.

### 18. What is Streamlit Community Cloud?
It is a hosting service that can deploy Streamlit applications from a connected source-code repository.

### 19. What is Git?
Git is a version-control system used to track changes to source code.

### 20. What is GitHub?
GitHub is a platform for hosting Git repositories and collaborating on software projects.

## Testing and Limitations

### 21. How is the application tested?
By uploading images, asking questions, checking the generated answers, testing conversation history, and verifying the deployed application.

### 22. What happens if the API key is missing?
The application cannot authenticate its API request and should display an appropriate error message.

### 23. What are the limitations?
The application depends on network access and API availability, and its answers may be inaccurate.

### 24. What is the future scope?
Possible improvements include persistent history, image comparison, support for multiple images, and expanded visual analysis.

### 25. What did you learn from this project?
The project demonstrates Python application development, API integration, image encoding, interactive web interfaces, version control, deployment, and basic security practices.
