# Outline:
1. main.py which will start and end the code
2. listen.py determine what is asked
3. response.py configure the responses for each request
   1. This is the one that determines what kind of task is requested
4. voice.py configure the voice assistant

**KEYS: ACTIONS**
TIME & WHAT: Time
DATE & WHAT: Date
UNTIL & HOW: How long until
WEATHER & WHAT: Weather
HIGH/LOW & WHAT: Specific day's weather
FORECAST & WHAT: Seven-day forecast
SEARCH FOR: Websearch (Google or Bing?)
HEY CHUCK: ChatGPT
NEWS & HEADLINES: News
JOKE & TELL: Joke
YOU & YOUR: Assistant

**Loging Branching**
"Hey Chuck"
"Search for"
"Joke tell"
"News"
"Joke"
"Weather"
"Time"
"Assistant"
"Random"
"Kitty terminal"

# Goals:
-  Time -> Date -> DoW
  - "What time is it?" _TIME_ 'WHAT'
  - "What is today's date?" _DATE_ 'WHAT'
    - Response would include the DoW and numerical answer as well
-  Days until
  - "How many days until?" _UNTIL_ 'HOW'
  - "How long until?" same --- hours and minutes too?
-  get weather
  - "What is today's weather?" _WEATHER_ 'WHAT'
  - "What is the high/low today?" _HIGH/LOW_ 'WHAT'
  - "What is the weather on {date}?" _WEATHER_ 'WHAT'
  - "What is the next seven-day forecast?" _FORECAST_ 'WHAT'
- basic calculator
- search web
  - "Search for {thing}" _SEARCH_ 'FOR'
  - "Search for: what is the largest animal?"
- ask questions to ChatGPT (tell stories, a joke, explanations)
  - "Hey Chuck: ..." _HEY CHUCK_
- generate art?
- check news headlines
  - "What's the news?" _NEWS_
  - "Headlines" _HEADLINES_
- tell a joke
  - "Tell me a joke" _JOKE_ 'TELL'
- check board game news
- automated email or message?
- to do list
- integrate with Obsidian
    - print out an explanation as a note?
- start timer: get current status
- set reminder
- repeat last output
- play music or audiobook?
- tune into a radio station
- trivia questions and game
- translate
- Lord of the Rings quotes?
- text to speech of an open document/webpage
- speech to text for open text box (email, Obsidian, etc.)
- open an app
- play mediation routine
- sunrise and moon cycle
