import speech_recognition as sr
import pyttsx3


# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

r = sr.Recognizer()
wordArray = []


while(True):
    try:
        with sr.Microphone(device_index=2) as source:
            print("adjusting for ambient nosie")
            r.adjust_for_ambient_noise(source, duration = 0.2)
            print("listening for audio")
            audio = r.listen(source)
            print("Captured audio, now interpreting it")

            text = r.recognize_google(audio, language = 'en-IN', show_all = True )
            arrayOfAnswers = text["alternative"]
            best = arrayOfAnswers[0]
            result = best["transcript"]
            print(result)

            temp = result.split()
            for i in temp:
                wordArray.append(i)
            print(wordArray)

    except:
        print("error")