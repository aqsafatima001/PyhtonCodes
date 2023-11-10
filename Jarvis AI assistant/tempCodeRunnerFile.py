def takeCommand():
    '''
    It takes microphone input from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language="en-in")
        print(f"User said: {query}\n")  #User query will be printed.
    except Exception as err:
        # print(err)
        print("Say that again...!")
        return "None"
    # speak(query)
    return query