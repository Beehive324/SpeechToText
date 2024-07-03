import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()


def record():
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                output_text = r.recognize_google_cloud(audio)

                return output_text

        except sr.RequestError as e:
            print(e)

        except sr.UnknownValueError as e:
            print("Error")


def output(text):
    f = open("audio.txt", "a")
    f.write(text)
    f.write("/n")
    f.close()

while True:
    text = record()
    output(text)

    print("...")