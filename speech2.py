import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    r3.adjust_for_ambient_noise(source)
    print("Search Google or YouTube")
    print('Speak anything : ')
    audio = r3.listen(source)
    print("Recognizing.....")
    t = r2.recognize_google(audio)
    print("You said {}".format(t))

    

if 'YouTube' in t:
    r2 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        r2.adjust_for_ambient_noise(source)
        print('Search your query')
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print("You said : {}".format(get))
            wb.get().open_new(url+get)

        except sr.UnknownValueError:
            print("ERROR")
        except sr.RequestError as e:
            print('Failed'.format(e))

if 'Google' in t:
    path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

    r1 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        r1.adjust_for_ambient_noise(source)
        print('Search your query')
        audio = r1.listen(source)

        try:
            text = r1.recognize_google(audio)
            print("You said : {}".format(text))
            wb.get(path).open_new(text)

        except sr.UnknownValueError:
            print("ERROR")
        except sr.RequestError as e:
            print('Failed'.format(e))




