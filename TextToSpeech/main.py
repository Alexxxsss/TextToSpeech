from gtts import gTTS
import os
from googletrans import Translator, constants
from pprint import pprint
import time

translator = Translator()
clear = lambda: os.system('cls')
clear()# clear console

textTTS = input("Write a sentence: ")


# --Variables-- #
fileF = ["wav","mp3","mp4"]
fs = 0
language = "en"
# --Variables-- #


clear() # clear console

myobj = gTTS(text=textTTS, lang=language, slow=fs) # creates a tts template

def lang():
    clear() # clear console
    language = input("sv\nen\nru\nfr\nde\Choose a language: ")
    clear() # clear console
    return language
def tran():
    global textTTS
    text = textTTS
    
    clear() # clear console
    language = input("sv\nen\nru\nfr\nde\nChoose a language: ")
    clear() # clear console
    
    translation = translator.translate(text, dest=language) # translate between languages
    return translation.text

def speed():
    clear() # clear console
    x = input("1: Fast\n2: Slow\nChoose a speed: ")
    clear() # clear console
    
    y = int(x) # convert to bool
    return y-1


while True:
    print("Text: "+textTTS+"\n"+f"Speech: {language}\n")
    alt=int(input("Settings\n1: Translate\n2: Speed\n3: Language(Speech)\n4: Done\nPick one: "))
    
    # --all options-- #
    if alt == 1:  textTTS = tran()
    if alt == 2: fs=speed()
    if alt == 3: language=lang()
    if alt == 4: 
        clear() # clear console
        FileName = input("File Name: ")
        form = int(input("1: .wav\n2: .mp3\n3: .mp4\nPick one: "))
        form = form-1
        break
    # --all options-- #
    
    myobj = gTTS(text=textTTS, lang=language, slow=fs) #apply options
    
    clear() # clear console
clear() # clear console
for i in range(5):
    for e in range(4):
        
        
        # --console animation-- #
        if e == 1: print(".")
        if e == 2: print(". .")
        if e == 3: print(". . .")
        time.sleep(0.2)
        # --console animation-- #
        clear() # clear console 
        
myobj.save(f"{FileName}."+fileF[form]) # File controll
os.system(f"{FileName}."+fileF[form]) # File controll

print(f"Done with downloading {FileName}."+fileF[form])
