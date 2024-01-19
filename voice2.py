# Author: Colton Crowther
# GitHub username: ojo4f3
# Date: 
# Description:

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


# txt_to_wav("test.txt", "test_1.wav")
txt_to_wav("It also works with a string instead of a file path", "response.wav", False)
