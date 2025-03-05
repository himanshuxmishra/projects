import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import webbrowser  # Use webbrowser to open URLs

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change index to 0 for male voice 1 for female voice

assistant_name = "ALEX"  # Set the name of your assistant here

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak(f"I am your voice assistant, {assistant_name} .")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query.lower()
    

def main():
    wish_me()
    while True:
        query = take_command()
        if 'whatsapp' in query :
            speak("Opening WhatsApp.")
            webbrowser.open("https://web.whatsapp.com/")
        elif 'youtube' in query:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com/")
        elif 'github' in query:
            speak("Opening GitHub.")
            webbrowser.open("https://www.github.com/")
        elif 'smash' in query:
            speak("Opening smashkarts.")
            webbrowser.open("https://smashkarts.io/")
        elif 'diterp' in query:
            speak("Opening Dit Erp.")
            webbrowser.open("https://erp.dituniversity.edu.in/")

        elif 'time' in query:
            now = datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {now}.")
        elif 'date' in query:
            today = datetime.today().strftime("%Y-%m-%d")
            speak(f"Today's date is {today}.")
         
        elif 'exit' in query or 'stop' in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()