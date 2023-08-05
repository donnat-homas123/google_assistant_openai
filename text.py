import os
import time
import pyaudio
import speech_recognition as sr
import playsound 
from gtts import gTTS
import openai
import uuid

api_key = "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"

lang ='en'

openai.api_key = api_key


guy = ""

while True:
    def get_adio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
                global guy 
                guy = said
                

                if "Google" in said:
                    ##words = said.split()
                    new_string=said.replace("Google","")
                    new_string = new_string.strip()
                    print(new_string) 
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content":said}])
                    text = completion.choices[0].message.content
                    speech = gTTS(text = text, lang=lang, slow=False, tld="com.au")
                    file_name= f"welcome_{str(uuid.uuid4())}.mp3"
                    speech.save(file_name)
                    playsound.playsound(file_name,block=False)
                    
            except Exception:
                print("Audio not clear!!!")


        return said

    if "stop" in guy:
        break


    get_adio()
