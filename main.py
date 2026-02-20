import os
import json

import sys
import os

sys.path.append(os.path.join(os.getcwd(), ".venv", "Lib", "site-packages"))

from groq import Groq  # Now it will find it!

current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. LIST ALL FILES in that folder to see what is actually there
files_in_folder = os.listdir(current_dir)
print(f"Files found in folder: {files_in_folder}")

# 3. SET YOUR FILENAME (Make sure this matches one of the names printed above!)
# Change 'YOUR_AUDIO.wav' to the actual name of your file
# Use the actual filename from your folder list
target_file = "YOUR_AUDI0.wav.m4a"
filename = os.path.join(current_dir, target_file)
# Initialize the Groq client
client = Groq(api_key="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")


with open(filename, "rb") as file:
    # Create a transcription of the audio file
    transcription = client.audio.transcriptions.create(
        file=file,  # Required audio file
        model="whisper-large-v3-turbo",  # Required model to use for transcription
        prompt="Specify context or spelling",  # Optional
        response_format="verbose_json",  # Optional
        timestamp_granularities=[
            "word",
            "segment",
        ],  # Optional (must set response_format to "json" to use and can specify "word", "segment" (default), or both)
        language="en",  # Optional
        temperature=0.0,  # Optional
    )
    # To print only the transcription text, you'd use print(transcription.text) (here we're printing the entire transcription object to access timestamps)
    print(json.dumps(transcription, indent=2, default=str))
