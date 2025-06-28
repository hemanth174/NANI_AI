import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import os
import sys

def talk(text):
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Use female voice
    print("🎙️ GIRI:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")    
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("🗣️ You said:", command)
    except sr.UnknownValueError:
        talk("Sorry bro, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""
    return command

def run_giri():
    while True:
        command = take_command()

        if "play" in command:
            try:
                import pywhatkit
                song = command.replace("play", "")
                talk("Playing on YouTube 🎶")
                pywhatkit.playonyt(song)
            except Exception as e:
                talk(f"Sorry, I can't play songs right now: {e}")

        elif "what's the time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"It’s {time} ⏰")

        elif "who is uday codes" in command or "who is uday_codes" in command:
            info = (
                "Uday, known as uday_codes on Instagram, is a coding content creator. "
                "He teaches Python projects in Telugu and runs udaycodes.in 💻"
            )
            talk(info)

        elif "who is" in command:
            person = command.replace("who is", "").strip()
            try:
                info = wikipedia.summary(person, sentences=1)
                talk(info)
            except:
                talk("Sorry, I couldn’t find information about that person.")

        elif "joke" in command:
            talk(pyjokes.get_joke())

        elif "open chrome" in command:
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            if os.path.exists(chrome_path):
                talk("Opening Chrome 🚀")
                os.startfile(chrome_path)
            else:
                talk("Chrome path not found 😬")
        elif "Hi GIRI" in command or "Hello GIRI" in command:
            talk("Hello there! How can I assist you today? 😊")
        elif "open youtube" in command:
            talk("Opening YouTube 🎥")
            os.system("start https://www.youtube.com")
        elif "open google" in command:
            talk("Opening Google 🌐")
            os.system("start https://www.google.com")
        elif "open notepad" in command:
            talk("Opening Notepad 📝")
            os.system("notepad")

        elif "open code" in command or "open vs code" in command:
            talk("Opening VS Code 💻")
            os.system("code")

        elif "exit" in command or "stop" in command:
            talk("Okay bro, see you later 👋")
            break

        elif command != "":
            talk("I heard you, but I don’t understand that yet 😅")

def run_giri_once():
    conversation = []
    conversation.append("🎧 Listening...")
    command = take_command()
    if command:
        conversation.append(f"🗣️ You said: {command}")
    else:
        conversation.append("🗣️ You said: ...")
    response = ""

    if "play" in command:
        try:
            import pywhatkit
            song = command.replace("play", "")
            response = "Playing on YouTube 🎶"
            talk(response)
            pywhatkit.playonyt(song)
        except Exception as e:
            response = f"Sorry, I can't play songs right now: {e}"
            talk(response)

    elif "what's the time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        response = f"It’s {time} ⏰"
        talk(response)

    elif "who is uday codes" in command or "who is uday_codes" in command:
        response = (
            "Uday, known as uday_codes on Instagram, is a coding content creator. "
            "He teaches Python projects in Telugu and runs udaycodes.in 💻"
        )
        talk(response)

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            response = wikipedia.summary(person, sentences=1)
        except:
            response = "Sorry, I couldn’t find information about that person."
        talk(response)

    elif "fun" in command:
        response = pyjokes.get_joke()
        talk(response)

    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            response = "Opening Chrome 🚀"
            talk(response)
            os.startfile(chrome_path)
        else:
            response = "Chrome path not found 😬"
            talk(response)

    elif "Hi GIRI" in command or "Hello GIRI" in command:
        response = "Hello there! How can I assist you today? 😊"
        talk(response)

    elif "open youtube" in command:
        response = "Opening YouTube 🎥"
        talk(response)
        os.system("start https://www.youtube.com")

    elif "open google" in command:
        response = "Opening Google 🌐"
        talk(response)
        os.system("start https://www.google.com")

    elif "open notepad" in command:
        response = "Opening Notepad 📝"
        talk(response)
        os.system("notepad")

    elif "open code" in command or "open vs code" in command:
        response = "Opening VS Code 💻"
        talk(response)
        os.system("code")

    elif "exit" in command or "stop" in command:
        response = "Okay bro, see you later 👋"
        talk(response)

    elif command != "":
        response = "I heard you, but I don’t understand that yet 😅"
        talk(response)

    conversation.append(f"🎙️ GIRI: {response}")
    return conversation

# talk("Yo! I'm GIRI – your personal voice assistant 💡")
# while False:
#     run_giri()