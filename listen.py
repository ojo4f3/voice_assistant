# Author: Colton Crowther
# GitHub username: ojo4f3
# Date: 03 APR 2023
# Description: 

import time
import speech_recognition as sr


class Ear:
    def __init__(self):
        self._ear = sr.Recognizer()

    def listen_up(self):
        with sr.Microphone() as source:
            try:
                audio_in = self._ear.listen(source, timeout=2, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                return None
            try:
                input_text = self._ear.recognize_google(audio_in)
                print(input_text)
                time.sleep(0.5)
                return input_text
            except sr.UnknownValueError or sr.RequestError:
                return None
