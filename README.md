# Multi Language CNIC Card Info Extractor LLM App using Google Gemini Pro Vision

This is an end-to-end application to extract information from CNIC cards using the Gemini Pro Vision model from Google. The application is built with Streamlit for the web interface.

## Features

- Extracts information from CNIC cards.
- Uses Google Gemini Pro Vision for content generation.
- Handles image uploads and displays extracted information.

## Prerequisites

- Python 3.8 or higher
- A Google API key with access to the Gemini Pro Vision model

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of the project and add your Google API key:

    ```env
    GOOGLE_API_KEY=your_google_api_key_here
    ```

To Run the application
```bash
streamlit run app.py
```

Project Demo
<img width="523" alt="Screenshot 2024-06-23 at 12 43 41 PM" src="https://github.com/ahmedashfaq850/End-to-End-Multi-Language-CNIC-Card-Info-Extractor-LLM-Application-Using-Gemini-Pro-Vision/assets/74646219/6c4dad5c-458c-4255-8fd4-9aaf880afe56">




