import os
import json
from groq import Groq

# Initialize the Groq client
client = Groq(api_key="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")

# Specify the path to the audio file
filename = (
    os.path.dirname(__file__) + "/YOUR_AUDI0.wav.m4a"
)  # Replace with your audio file!

# Open the audio file
with open(filename, "rb") as file:
    # Create a translation of the audio file
    translation = client.audio.translations.create(
        file=(filename, file.read()),  # Required audio file
        model="whisper-large-v3",  # Required model to use for translation
        prompt="Specify context or spelling",  # Optional
        # Optional ('en' only)
        response_format="json",  # Optional
        temperature=0.0,  # Optional
    )
    # Print the translation text
    print(translation.text)
