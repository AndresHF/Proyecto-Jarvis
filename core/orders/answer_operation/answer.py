import jarvisCore as jc
from bs4 import BeautifulSoup as soup
from core.orders.system.volume import *
from core.orders.system.notes import *
from core.orders.web_operations import scraping
from core.orders.constants import *

weatherLabels = [
    {"label": "span", "obj": {"class": "c-tib-text"}},
    {"label": "span", "obj": {"class": "m_table_weather_day_max_temp"}},
    {"label": "span", "obj": {"class": "m_table_weather_day_min_temp"}},
    {"label": "section", "obj": {"class": "-block-4"}},
    {"label": "section", "obj": {"class": "-block-5"}},
]


def answerQuestion(order):
    if "volumen" in order:
        jc.jarvisTalk("El volumen está actualmente al " + getActualVolume() + " %")
    elif "qué" in order or "que" in order:
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
    elif "nota" in order or "notas" in order:
        knowThings(order)


def knowThings(order):
    if "notas" in order or "nota" in order:
        notesOperations(order)
    elif "hora es" in order:
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

            weatherInfo = scraping.getMultipleLabels(
                "https://www.eltiempo.es/", city, weatherLabels, ".html"
            )
            stringTemplate = "La temperatura de {} es de {} grados con máximas de {} y mínimas de {}. Vientos de {} kilómetros. {}. La sensación térmica es de {} grados."
            sensation = ""
            try:
                sensation = scraping.findWeatherInfo(
                    weatherInfo[4].find_all("p")[1].span, "data-temp"
                )
            except:
                sensation = scraping.findWeatherInfo(weatherInfo[0], "data-temp")
            wind = ""
            try:
                wind = scraping.findWeatherInfo(
                    weatherInfo[4].find_all("p")[3].span, "data-wind"
                )
            except:
                wind = scraping.findWeatherInfo(
                    weatherInfo[4].find_all("p")[1].span, "data-wind"
                )
            jc.jarvisTalk(
                stringTemplate.format(
                    city,
                    scraping.findWeatherInfo(weatherInfo[0], "data-temp"),
                    scraping.findWeatherInfo(weatherInfo[1].span, "data-temp"),
                    scraping.findWeatherInfo(weatherInfo[2].span, "data-temp"),
                    wind,
                    weatherInfo[3].text,
                    sensation,
                )
            )

        except:
            jc.jarvisTalk("No tengo información sobre " + city)


def getLastWord(order):
    splittedOrder = order.split(" ")
    return splittedOrder[len(splittedOrder) - 1]


def splitByCutter(order, cutter):
    return order.split(cutter)[1].strip()

