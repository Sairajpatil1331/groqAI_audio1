GroqAI Audio & Data Toolkit 🎙️⚡
Overview
A robust, Python-based Data Science and Generative AI pipeline designed to handle advanced audio processing and dynamic API data fetching. Developed as part of an active Data Science internship at The Skybrisk, this repository demonstrates end-to-end integration with the Groq Cloud API and third-party REST APIs.

Core Features
Audio Transcription: Highly accurate, timestamped speech-to-text processing utilizing the whisper-large-v3 model.

Audio Translation: Automated conversion of foreign language audio files directly into English text.

Text-to-Speech (TTS): Human-like audio generation using Canopy Labs' orpheus-v1-english model.

Dynamic Data Pipelines: Includes scripts for fetching, parsing, and evaluating real-time JSON data (e.g., global weather metrics) using standard web requests.

Secure Configuration: Implements python-dotenv and .env architecture to securely manage API credentials and prevent key leakage.

Tech Stack
Language: Python 3.x

Libraries: groq, requests, python-dotenv

Models: whisper-large-v3, orpheus-v1-english
