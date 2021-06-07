import speech_recognition as sr
import playsound
from gtts import gTTS
import random
import webbrowser
import os
import pyautogui
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


class person:
    name = ''

    def setName(self, name):
        self.name = name


class asis:
    name = ''

    def setName(self, name):
        self.name = name



def talk(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()


def talk(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(asis_obj.name + ":", audio_string)
    os.remove(audio_file)

def take_command():
    try:
        with sr.Microphone() as source:
            print('How may i help ?')
            talk('How may i help ?')
            voice = listener.listen(source)
            command =listener.recognize_google(voice)
            command = command.lower(voice)
            if 'Tess' in command:
                command = command.replace('Tess', '')
                print(command)

    except:
        pass
    return command


def run_Tess():
    command = take_command()
    print(command)


# play music on youtube
    if'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        print('playing ' + song)
        pywhatkit.playonyt(song)


# what is the time ?
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        talk('Current time is ' + time)
        print(time)


# wikipedia
    elif 'what is' in command:
        meaning = command.replace('what is', '')
        info = wikipedia.summary(meaning, 1)
        print(info)
        talk(info)


# Need some Computer eng. Jokes
    elif 'joke' in command:
        talk(pyjokes.get_joke())

# Greeting
    elif ('hey', 'hi', 'hello', 'hai', 'yo', 'Tess') in command:
        greetings = ["hey, how can i help out" + person_obj.name, "Hey, what's up?" + person_obj.name,
                     "I'm all ears" + person_obj.name, "How can i help you?" + person_obj.name,
                     "Hello" + person_obj.name]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        talk(greet)


# Greeting 2
    elif(["how are you", "how are you doing"]) in command:
        talk("I'm very well, thanks for asking " + person_obj.name)


# Google Search
    elif(["search for"]) in command and 'youtube' not in command:
        search_term = command.split("search for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        talk("Here is what I found for" + search_term + "on google")


# Know the stocks
    elif(["price of"]) in command:
        search_term = command.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        talk("Here is what I found for " + search_term + " on google")

# Want some IG
    elif(["open instagram", "want to have some fun time"]) in command:
            search_term = command.split("for")[-1]
            url = "https://www.instagram.com/"
            webbrowser.get().open(url)
            talk("opening instagram")


# What's the weather
    elif(["weather", "tell me the weather report", "whats the condition outside"]) in command:
        search_term = command.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        talk("Here is what I found for on google")


# Let's see some mails
    elif (["open my mail", "gmail", "check my email"]) in command:
        search_term = command.split("for")[-1]
        url = "https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        talk("here you can check your gmail")


# Want a game to play

    elif (["game"]):
        command = take_command("choose among rock paper or scissor")
        moves = ["rock", "paper", "scissor"]

        cmove = random.choice(moves)
        pmove = command

        talk("The computer chose " + cmove)
        talk("You chose " + pmove)
        # engine_speak("hi")
        if pmove == cmove:
            talk("the match is draw")
        elif pmove == "rock" and cmove == "scissor":
            talk("You wins")
        elif pmove == "rock" and cmove == "paper":
            talk("I won")
        elif pmove == "paper" and cmove == "rock":
            talk("You wins")
        elif pmove == "paper" and cmove == "scissor":
            talk("I won")
        elif pmove == "scissor" and cmove == "paper":
            talk("You wins")
        elif pmove == "scissor" and cmove == "rock":
            talk("I won")


# Toss a coin Tess
    elif(["toss", "flip", "coin"]) in command:
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        talk("The computer chose " + cmove)


# Calculate Tess
    elif (["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/"]):
        opr = command.split()[1]

        if opr == '+':
            talk(int(command.split()[0]) + int(command.split()[2]))

        elif opr == '-':
            talk(int(command.split()[0]) - int(command.split()[2]))
        elif opr == 'multiply':
            talk(int(command.split()[0]) * int(command.split()[2]))
        elif opr == 'divide':
            talk(int(command.split()[0]) / int(command.split()[2]))
        elif opr == 'power':
            talk(int(command.split()[0]) ** int(voice_data.split()[2]))
        else:
            talk("Wrong Operator")







person_obj = person()
asis_obj = asis()
asis_obj.name = 'TESS'
engine = pyttsx3.init()



run_Tess()
