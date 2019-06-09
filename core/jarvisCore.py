import speech_recognition as sr

import pyaudio
import wave
import subprocess
import pyttsx3
import time
import webbrowser
import sys
from random import randint

from gtts import gTTS

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from unicodedata import normalize

from orders.system import volume

from orders.web_operations import find
from orders.web_operations import *

from orders.answer_operation import answer
from talk.constants import *
from orders.constants import *


engine = pyttsx3.init("espeak")

voices = engine.getProperty("voices")
engine.setProperty("voice", "spanish")

engine.setProperty("rate", 200)  # Speed percent (can go over 100)
engine.setProperty("volume", 0.9)  # Volume 0-1

r = sr.Recognizer()
r.energy_threshold = 4000


def launchReactNative():
    subprocess.Popen(['xterm -e "native"'], shell=True, stdout=subprocess.PIPE)


def closeComputer():
    subprocess.call("init 0", shell=True)


def initOrderProtocol(order):
    if "nativo" in order:
        jarvisTalk("Iniciando React Native, happy codding nigah!")
        launchReactNative()
    elif any(word in order for word in unkownAnswer):
        jarvisTalk(elocuentNegation[randint(0, len(elocuentNegation) - 1)])


# --------------------- COMUNICATION FUNCTIONS ----------------------------------------------------------------
def jarvisTalk(speech):
    fileName = "./core/recordings/temp.mp3"
    file = gTTS(speech, "es-es")
    file.save(fileName)
    subprocess.call(["cvlc", "--play-and-exit", fileName])
    # time.sleep(voice.duration)
    # engine.say(speech)
    # engine.runAndWait()
    # engine.stop()


def listen(message=""):
    with sr.Microphone() as source:
        if len(message) > 0:
            jarvisTalk(message)
        print("..")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            print("...")
            text = r.recognize_google(audio, language="es-ES")
            print("You said: {}".format(text))
            return text + ""

        except sr.UnknownValueError:
            return "Estoy a la escucha"


def recieveOrder(dur=0, message=""):
    with sr.Microphone() as source:
        jarvisTalk(message)
        print("**")
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, duration=dur)
        try:
            print("****")
            text = r.recognize_google(audio, language="es-ES")

            return text

        except:
            return "Estoy a la escucha"


# --------------------------------------- PROTOCOLS SECTION ----------------------------------------------------------
def answerQuestionsProtocol(order):
    order = order.lower()
    answer.answerQuestion(order)


def searchInBrowserProtocol(order):
    try:
        order = order.lower()
        if "wikipedia" in order:
            find.findInWikipedia(order)
        elif "google" in order:
            find.findInGoogle(order)
        elif "maps" in order:
            find.findInMaps(order)
        elif "sistema" in order:
            word = answer.getLastWord(order)
            if word is "project":
                word += "s"
            subprocess.Popen(
                ['xterm -e "display ' + word + '"'], shell=True, stdout=subprocess.PIPE
            )
        else:
            find.findInGoogle(order, "busca")
    except:
        jarvisTalk("Faltan parametros en la búsqueda")


def setProtocol(order):
    order = order.lower()
    try:
        if "volumen" in order:
            volume.setVolume(order)
        elif "alarma" in order:
            time = order.split(" ")[len(order.split(" ")) - 1]
            hour = time.split(":")[0]
            minute = ""
            if ":" in time:
                minute = " " + time.split(":")[1]
            subprocess.Popen(
                ["alarm " + hour + minute], shell=True, stdout=subprocess.PIPE
            )
        else:
            find.searchAndPlay(order, "pon")
    except:
        jarvisTalk("Error en los parámetros")


def closingProtocol(order):
    order = order.lower()
    if "chrome" in order:
        subprocess.Popen(["killall chrome"], shell=True, stdout=subprocess.PIPE)
    elif "firefox" in order:
        subprocess.Popen(["killall firefox"], shell=True, stdout=subprocess.PIPE)
    elif "code" in order or "kodi" in order:
        subprocess.Popen(["killall code"], shell=True, stdout=subprocess.PIPE)

