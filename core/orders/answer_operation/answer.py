import jarvisCore as jc
from bs4 import BeautifulSoup as soup
from core.orders.system.volume import *
from core.orders.web_operations import scraping
from core.orders.constants import *


def answerQuestion(order):
    if "volumen" in order:
        jc.jarvisTalk("El volumen está actualmente al " + getActualVolume() + " %")
    elif "qué" in order:
        knowThings(order)
    elif "chiste" in order:
        label = scraping.getLabel(
            "https://chistescortos.yavendras.com/", "", "p", "description", "", "all"
        )
        jc.jarvisTalk(scraping.findJoke(label))
    elif "quién eres" in order:
        jc.jarvisTalk(whoAmI)
    elif "cuál es tu propósito" in order:
        jc.jarvisTalk(purpose)
    elif "haces" in order:
        jc.jarvisTalk(how)


def knowThings(order):
    if "hora es" in order:
        getTimeAsByteArr = subprocess.Popen(
            ["date '+%X'"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True
        )
        timeAsCharArr = getTimeAsByteArr.communicate(b"' stdin")[0]
        jc.jarvisTalk("".join(map(chr, timeAsCharArr)))
    elif any(word in order for word in knowingThingsConstants):
        try:

            label = scraping.getLabel(
                "https://www.wordreference.com/definicion/",
                getLastWord(order),
                "ol",
                {"class": "entry"},
            )

            jc.jarvisTalk(scraping.findInDictionary(label))
        except:
            jc.jarvisTalk("No tengo ni idea de lo que es")
    elif any(word in order for word in weatherConstants):
        try:

            city = "-".join(splitByCutter(order, "en").split(" "))
            label = scraping.getLabel(
                "https://www.eltiempo.es/",
                city,
                "span",
                {"class": "c-tib-text"},
                ".html",
            )
            jc.jarvisTalk(
                "La temperatura de "
                + city
                + " es de "
                + scraping.findWeather(label)
                + " grados"
            )
        except:
            jc.jarvisTalk("No tengo información sobre " + city)


def getLastWord(order):
    splittedOrder = order.split(" ")
    return splittedOrder[len(splittedOrder) - 1]


def splitByCutter(order, cutter):
    return order.split(cutter)[1].strip()

