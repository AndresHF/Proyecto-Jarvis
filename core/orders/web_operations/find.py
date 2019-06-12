import subprocess
from orders.web_operations import scraping
import core.jarvisCore as jc
from core.orders.constants import *
from core.talk.constants import *
import random

youtubeLastOrder = None


def findInGoogle(order, splitWord="google"):
    googleSearch = order.split(splitWord)[1]
    search = "+".join(googleSearch.split(" "))
    url = "https://www.google.com/search?q=" + search
    subprocess.Popen(
        ["google-chrome " + url + " &"], shell=True, stdout=subprocess.PIPE
    )


def findInMaps(order):
    # To use this function, is required to recieve an order like ["place to find"] ["village"](1 word) ["city"]
    # Otherwise we are going to find a wrong result or throw a "Parameter error"
    # Example: busca en Maps tiendas de ropa cerca de Boadilla Madrid
    # So we start taking what we need splitting by "maps " -> tiendas de ropa cerda de Boadilla Madrid
    mapSearch = order.split("maps ")[1]

    # directionChunkA is going to be the ["village"] -> "Boadilla"
    directionChunkA = mapSearch.split(" ")[len(mapSearch.split(" ")) - 2]

    # directionChunkB is going to be the ["city"] -> "Madrid"
    directionChunkB = mapSearch.split(" ")[len(mapSearch.split(" ")) - 1]

    # toSearch is going to be the thing to find in Google Maps --> "tiendas de ropa cerca de"
    # If the order is properly builded we find it by splitting our "mapSearch" by the "village" at position [0]
    # We need to join it with "+" to make a proper Google Maps URL at a browser --> tiendas+de+ropa+cerca+de
    toSeatch = "+".join(mapSearch.split(directionChunkA)[0].split(" "))

    # After that we join all together to be ready to open a browser
    # The final result is going to be https://www.google.es/maps/search/Tiendas+De+Ropa+Cerca+De+,+Boadilla,+Madrid
    # Its needed to capitalice with str.title() function because it avoid having problems with our URL
    url = (
        "https://www.google.es/maps/search/"
        + toSeatch.title()
        + ",+"
        + directionChunkA.title()
        + ",+"
        + directionChunkB.title()
    )

    # So its time to open our browser with the URL Google Maps likes to use
    subprocess.Popen(
        ["google-chrome " + url + " &"], shell=True, stdout=subprocess.PIPE
    )


def findRoutes():
    jc.jarvisTalk("Establece un punto de partida")
    origin = jc.listen()
    jc.jarvisTalk("Añade un destino")
    destination = jc.listen()
    moreDestinations = []
    answer = ""
    jc.jarvisTalk("Para finalizar di. Finalizar ruta")
    while "finalizar ruta" not in answer:
        try:
            jc.jarvisTalk(random.choice(destinations))
            answer = jc.listen()
            if len(answer) > 0 and "finaliza" not in answer:
                jc.jarvisTalk(random.choice(destinationAnswer))
                moreDestinations.append(jc.listen())
            elif "finaliza" not in answer:
                jc.jarvisTalk("No has dicho nada")
        except:
            jc.jarvisTalk(random.choice(iDontUnderstand))
    jc.jarvisTalk("Petición finalizada. Buscando rutas.")
    url = (
        "https://www.google.es/maps/dir/"
        + ",+".join(origin.split(" "))
        + "/"
        + ",+".join(destination.split(" "))
    )

    for dest in moreDestinations:
        url += "/" + ",+".join(dest.split(" "))

    subprocess.Popen(["google-chrome " + url + " &"], shell=True)
    jc.jarvisTalk("¡Buen viaje!")


def findInWikipedia(order):
    wikiSreach = order.split("wikipedia")[1]
    search = "_".join(wikiSreach.split(" ")).title()
    url = "https://es.wikipedia.org/wiki/" + search
    subprocess.Popen(["google-chrome " + url + " &"], shell=True)


def searchAndPlay(order, cutter="música"):
    order = order.lower()
    global youtubeLastOrder
    realPetition = order.split(cutter)[1].strip()
    if youtubeLastOrder is not None:
        # in case we already openned a YouTube video we should close it first, it´s annoying to have two videos playin at same time
        try:
            # first step is look for our video getting all web browser process
            popen = subprocess.Popen(
                [
                    'wmctrl -l | egrep -i "YouTube" | egrep -i "'
                    + youtubeLastOrder
                    + '"'
                ],
                shell=True,
                stdout=subprocess.PIPE,
            )
            output = popen.communicate(b"' stdin")[0]
            line = "".join(map(chr, output)).split("jaguars-M14xR1")[1].strip()

            # so we close it looking for last video oppened
            subprocess.call(['wmctrl -c "' + line + '"'], shell=True)
        except:
            # or close last founded in case we fail
            subprocess.call(["wmctrl -c YouTube"], shell=True)

    # we need to keep track of last petition, so we can close youtube with wmctrl linux command controller
    youtubeLastOrder = realPetition

    # after that we get our link by scrapYoutubeWatchURL() method
    link = scraping.scrapYoutubeWatchURL(order, cutter)

    # then we open it
    subprocess.call(["google-chrome --new-window " + link + " &"], shell=True)
