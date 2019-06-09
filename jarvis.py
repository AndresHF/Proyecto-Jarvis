import time
import sys
import subprocess

sys.path.insert(0, "/home/jaguars/projects/jarvis_1/core")
import threading
import jarvisCore as jc
from random import randint
from core.talk.constants import *
from core.orders.constants import *
from core.orders.system.recording import *
import core.orders.web_operations.scraping as sc

mainThread = True

while mainThread:
    if "María" in jc.listen().strip():
        newOrder = jc.listen(
            awaitingOrders[randint(0, len(awaitingOrders) - 1)]
        ).strip()
        print("NEW ORDER " + newOrder)
        if any(x in newOrder for x in disconectingOrders):
            mainThread = False
            jc.jarvisTalk("Desconectando programa...")

        elif "iniciar" in newOrder:
            jc.initOrderProtocol(newOrder)

        elif "busca" in newOrder:
            jc.searchInBrowserProtocol(newOrder)

        elif (
            any(order in newOrder for order in answerQuestionOrders)
            or "cuál" in newOrder
        ):
            jc.answerQuestionsProtocol(newOrder)

        elif "cierra" in newOrder:
            jc.closingProtocol(newOrder)

        elif "graba " in newOrder:
            recordConversation()

        elif "reproduce" in newOrder:
            playConversation()

        elif any(order in newOrder for order in setOrders):
            jc.setProtocol(newOrder)

        elif "hazte la loca" in newOrder:
            jc.jarvisTalk(crazyMode[randint(0, len(crazyMode) - 1)])

        elif "apaga el ordenador" in newOrder:
            jc.jarvisTalk("Apagando el ordenador")
            mainThread = False
            jc.closeComputer()

        else:
            jc.jarvisTalk(iDontUnderstand[randint(0, len(iDontUnderstand) - 1)])
    time.sleep(0.5)

