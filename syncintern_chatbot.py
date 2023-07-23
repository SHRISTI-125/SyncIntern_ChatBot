import SpeechRecognition as sp
import time
import random


print("Hi~ Shristi What's up. How may I help u")

r = sp.Recognizer()
with sp.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    t = r.recognize_google(audio)
    z="{}".format(t)
    print("z",z)
    print("you said : {}".format(t))
    try:
        text = r.recognize_google(audio)
        z=("You said : {}".format(text))
        print(z)

    except:
        print("Sorry could not recognize what you said")

processing = 1
while processing == 1:
    r = sp.Recognizer()
    with sp.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        t = r.recognize_google(audio)
        z="{}".format(t)
        print("z",z)
        print("you said : {}".format(t))
    m=z
    print(m)
    d={"greeting":["Hello!", "hi There!", "Hi this is Wuzzu the chatbot", "HI!"], "what is your name":["This is Wuzzu ~ The ChatBot", "Wuzzu ChatBot this side", "Wuzzu"],"thank you":["You're Welcome","Welcome","Mentioned not","Okay"]}
    dw={"are you not hearing me":["nah! I am hearing you!","I'm hearing"]}
    dz={"what do you do":"I am trying to give information.", "are you hearing me":"Yes Shristi" , "year in which python introduced":"1990 by Guido Van Rossum" , "how many modules do python have":"200 modules"}
    if m == "greeting" or m == "what is your name" or m =="thank you":
        k=random.choice(d[m])
    elif m == "are you not hearing me":
        k=random.choice(dw[m])
    else:
        k=dz[m]
    print(k)

    print("Want to say more")
    print("Do you wannt to say more")

    #saying = input("Enter yes or no")
    with sp.Microphone() as source1:
        audio1 = r.listen(source1)
        say = r.recognize_google(audio1)
        says = "{}".format(say)
    print(says)
if says == "yes":
    processing = 1
else:
    processing = 0
