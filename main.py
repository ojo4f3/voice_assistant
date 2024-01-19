# Author: Colton Crowther
# GitHub username: ojo4f3
# Date: 01 APR 2023
# Description:

import keyboard
from voice import Voice
from listen import Ear
from sort import Sorter


class Assistant:
    def __init__(self, speech_module, voice=0):
        # Start voice assistant's voice
        self._voice = Voice(speech_module, voice)
        welcome_text = "Hello Colton. How can I help you?"
        self._voice.speak(welcome_text)
        # Start voice assistant's listener
        self._ear = Ear()
        self._response = Sorter()
        self.hotkey_listener()

    def listen_response_loop(self):
        input_message = self._ear.listen_up()
        if input_message is not None:
            response = self._response.determine_request_type(input_message)
            self._voice.speak(response)

    def hotkey_listener(self):
        keyboard.add_hotkey('win+0', self.listen_response_loop)
        while True:
            try:
                keyboard.wait()
            except KeyboardInterrupt:
                break
            keyboard.clear_hotkey('win+0')
            print('hotkey reset')


if __name__ == "__main__":
    steve = Assistant('comtypes')

# import datetime
# import webbrowser

# # Define functions for performing tasks
# def set_reminder():
#     engine.say("What would you like me to remind you about?")
#     engine.runAndWait()
#     with sr.Microphone() as reminder_source:
#         reminder_audio = r.listen(reminder_source)
#         try:
#             reminder_text = r.recognize_google(reminder_audio)
#             engine.say("When would you like to be reminded?")
#             engine.runAndWait()
#             reminder_audio = r.listen(reminder_source)
#             try:
#                 reminder_time = r.recognize_google(reminder_audio)
#                 reminder_time = datetime.datetime.strptime(reminder_time, '%H:%M:%S')
#                 current_time = datetime.datetime.now().time()
#                 time_diff = datetime.datetime.combine(datetime.date.today(), reminder_time) -
#                 datetime.datetime.combine(
#                     datetime.date.today(), current_time)
#                 reminder_seconds = time_diff.seconds
#                 if reminder_seconds > 0:
#                     engine.say(f"I will remind you about {reminder_text} in {time_diff}")
#                     engine.runAndWait()
#                     # Code to set the reminder here
#                 else:
#                     engine.say("I'm sorry, that time has already passed.")
#                     engine.runAndWait()
#             except:
#                 engine.say("I'm sorry, I couldn't understand the time.")
#                 engine.runAndWait()
#         except:
#             engine.say("I'm sorry, I couldn't understand the reminder.")
#             engine.runAndWait()
#
#
# def create_todo_list():
#     engine.say("What tasks would you like to add to your to-do list?")
#     engine.runAndWait()
#     with sr.Microphone() as source:
#         audio = r.listen(source)
#         try:
#             todo_text = r.recognize_google(audio)
#             engine.say(f"Adding {todo_text} to your to-do list.")
#             engine.runAndWait()
#             # Code to add the task to the to-do list here
#         except:
#             engine.say("I'm sorry, I couldn't understand the task.")
#             engine.runAndWait()
#
#
# def search_web():
#     engine.say("What would you like me to search the web for?")
#     engine.runAndWait()
#     with sr.Microphone() as source:
#         audio = r.listen(source)
#         try:
#             search_text = r.recognize_google(audio)
#             engine.say(f"Searching the web for {search_text}.")
#             engine.runAndWait()
#             webbrowser.open(f"https://www.google.com/search?q={search_text}")
#         except:
#             engine.say("I'm sorry, I couldn't understand the search term.")
#             engine.runAndWait()
#
#
# # Main loop for the voice assistant
# while True:
#
#     engine.say("How can I help you?")
#     engine.runAndWait()
#     with sr.Microphone() as source:
#         audio = r.listen(source)
#         try:
#             text = r.recognize_google(audio)
#             if "reminder" in text:
#                 set_reminder()
#             elif "to-do list" in text:
#                 create_todo_list()
#             elif "search" in text:
#                 search_web()
#             elif "stop" in text or "exit" in text or "quit" in text:
#                 engine.say("Goodbye!")
#                 engine.runAndWait()
#         except:
#             break
#
