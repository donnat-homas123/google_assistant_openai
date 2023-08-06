# Project Name: google_assistant_openai
Through this project the ai assistant named google will capture the voice of user and displays it on screen
## Team members
1.Amita Treasa Wilfred [https://github.com/amitawilfred]

2.Donna Thomas [https://github.com/donnat-homas123]

3.Sanin Mohammed N [https://github.com/sanu00007]

# Speech Recognition with OpenAI and Flask

This repository contains a simple web application that uses Flask, OpenAI, and the Google Speech Recognition API to enable real-time speech recognition. The application captures audio from the user's microphone, sends it to the Google Speech Recognition API for recognition, and then processes the recognized text using OpenAI's GPT-3.5 model. The recognized text is displayed on the terminal.

## How it Works

1. When the user clicks on the "Start Recording" button, the web application captures audio from the user's microphone using the `speech_recognition` library.
2. The captured audio is sent to the Google Speech Recognition API for recognition, and the recognized text is extracted.
3. The recognized text is displayed on the terminal.

## Prerequisites

To run this application locally, you'll need the following:

- Python (>= 3.6)
- Flask (>= 2.0.0)
- PyAudio (>= 0.2.11)
- SpeechRecognition (>= 3.8.1)
- Playsound (>= 1.2.2)
- gTTS (>= 2.2.3)
- OpenAI GPT-3 API key

## Setup and Usage

1. Clone this repository to your local machine.

2. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt

