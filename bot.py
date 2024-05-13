# Importing necessary libraries
import google.generativeai as genai
import numpy as np
import pandas as pd
from dotenv import load_dotenv
import os

# Loading environment variables
load_dotenv()

# Configuring API key
genai.configure(api_key=os.getenv('API_KEY'))

# Setting up model generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

# Safety settings for content generation
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Initializing the generative model
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Starting a conversation with the generative model
convo = model.start_chat(history=[])

# Chat loop
prompt = ""
while prompt != "fim":
    prompt = input("Digite sua pergunta: ")
    convo.send_message(prompt)
    print(convo.last.text)
