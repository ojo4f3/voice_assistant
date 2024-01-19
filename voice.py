# Author: Colton Crowther
# GitHub username: ojo4f3
# Date: 03 APR 2023
# Description:

import pyttsx3
from gtts import gTTS
import elevenlabslib as el
from pydub import AudioSegment
from pydub.playback import play


class Voice:
    def __init__(self, module, voice=0):
        self._engine = module
        self._voice = voice
        self._assistant = None
        if self._engine == 'pyttsx3':
            self.initialize_voice()

    def initialize_voice(self):
        self._assistant = pyttsx3.init(driverName='sapi5')
        voices = self._assistant.getProperty('voices')
        self._assistant.setProperty('voice', voices[self._voice].id)
        self._assistant.setProperty('rate', 200)

    def speak(self, message):
        if self._engine == 'pyttsx3':
            self._assistant.say(message)
            self._assistant.runAndWait()
        elif self._engine == 'gTTS':
            speech_content = gTTS(text=message, lang='en', tld='com', slow=False)
            speech_content.save('message.mp3')
            play(AudioSegment.from_mp3('message.mp3'))
        elif self._engine == 'elevenlabs':
            user = el.ElevenLabsUser("6410a00e132378698021ebd09c471853")
            voice = user.get_voices_by_name("Steve")[0]  # This is a list because multiple voices can have the same name
            voice.generate_and_play_audio(message, playInBackground=False)
            # Clean up
            user.get_history_items()[0].delete()
        elif self._engine == 'comtypes':
            txt_to_wav(message, 'response.wav', False)
            play(AudioSegment.from_wav('response.wav'))


def txt_to_wav(text_input, output, text_from_file=True, speed=2, voice_name="David"):
    from comtypes.client import CreateObject
    engine = CreateObject("SAPI.SpVoice")

    engine.rate = speed  # from -10 to 10

    for voice in engine.GetVoices():
        if voice.GetDescription().find(voice_name) >= 0:
            engine.Voice = voice
            break
    else:
        print("Error voice not found -> default will be used.")

    if text_from_file:
        file = open(text_input, 'r')
        text = file.read()
        file.close()
    else:
        text = text_input

    stream = CreateObject("SAPI.SpFileStream")
    from comtypes.gen import SpeechLib

    stream.Open(output, SpeechLib.SSFMCreateForWrite)
    engine.AudioOutputStream = stream
    engine.speak(text)

    stream.Close()

# "Emily it's time to set up your bed. Time for bed! Get ready! Emily go brush your teeth. Go to the "bathroom. Find
#       your pillows. Quickly! Emily likes to drink fridge water with ice at night and loves her leaf blanket. Go get
#       your leaf blankey."
# "Emily would you like an ice cream cone? You are a nice sweetheart. Effie loves to eat ice cream and so there isn't
# any more mint chocolate chip left and Allison ate the rest of the other ice creams."

# "Emily would you like an ice cream cone? You are a nice sweetheart. Effie loves to eat ice cream and so there isn't
#       any more mint chocolate chip left and Allison ate the rest of the other ice creams."
# gTTS - tlds = ["us"]  # "co.uk", "com.au", "ie"]
