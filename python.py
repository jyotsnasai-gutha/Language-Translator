import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound

# Available translation options
LANGUAGES = {
    "1": ("French", "fr"),
    "2": ("Spanish", "es"),
    "3": ("German", "de"),
    "4": ("Hindi", "hi"),
    "5": ("Japanese", "ja"),
    "6": ("Tamil", "ta"),
    "7": ("Telugu", "te")
}

def show_language_menu():
    print("\nChoose a language to translate into:")
    for key, (name, _) in LANGUAGES.items():
        print(f"{key}. {name}")
    choice = input("Enter the number of your choice: ")
    return LANGUAGES.get(choice, ("French", "fr"))  # default: French

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio, language='en-US')
        print("You said:", text)

        # Language choice
        language_name, language_code = show_language_menu()

        # Translate
        translator = Translator()
        translation = translator.translate(text, dest=language_code)
        print(f"Translated to {language_name}:", translation.text)

        # Convert to speech
        converted_audio = gTTS(translation.text, lang=language_code)
        converted_audio.save("hello.mp3")
        playsound.playsound("hello.mp3")

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print(f"Speech recognition error: {e}")
    except Exception as e:
        print("An error occurred:", str(e))

# Run the main function
main()
