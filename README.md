# Project Name: google_assistant_openai
Through this project the ai assistant named google will capture the voice of user and displays it on terminal and audio is saved if the word "Google" is in the voice of user and the text is then read out by the ai assisstant .

## Team members
1.Amita Treasa Wilfred [https://github.com/amitawilfred]

2.Donna Thomas [https://github.com/donnat-homas123]

3.Sanin Mohammed N [https://github.com/sanu00007]


##Team Name
GOOGLY

## Link To Video
https://www.kapwing.com/videos/64cfd2c6a2c603007634e579

# Speech Recognition with OpenAI and Flask

This repository contains a simple web application that uses Flask, OpenAI, and the "Google" Speech Recognition API to enable real-time speech recognition. The application captures audio from the user's microphone, sends it to the Google Speech Recognition API for recognition, and then processes the recognized text using OpenAI's GPT-3.5 model. The recognized text is displayed on the terminal.

## How the tool works


1. When the user clicks on the "Start Recording" button, the web application captures audio from the user's microphone using the `speech_recognition` library.
2. The captured audio is sent to the Google Speech Recognition API for recognition, and the recognized text is extracted.
3.  If the recognized text contains the keyword "Google", it is sent to OpenAI's GPT-3.5 model using the `openai` Python library to generate a response.
4. The generated response from OpenAI is converted to speech using the `gtts` library, and the audio file is saved.
5. The recognized text is displayed in the terminal and the audio response can be hear.



## Libraries Used

To run this application locally, you'll need the following:

- Python (>= 3.6)
- Flask (>= 2.0.0)
- PyAudio (>= 0.2.11)
- SpeechRecognition (>= 3.8.1)
- Playsound (>= 1.2.2)
- gTTS (>= 2.2.3)
- OpenAI GPT-3 API key

## How to configure and Run

1. Clone this repository to your local machine.

2. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
3. To run the code type:-
    python server.py    

