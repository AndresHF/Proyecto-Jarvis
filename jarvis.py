import time
import sys
import subprocess

sys.path.insert(0, "./core")
import core.jarvisCore as jc
from random import choice
from core.talk.constants import *
from core.orders.constants import *
from core.orders.system.recording import *
import core.orders.web_operations.scraping as sc

mainThread = True

while mainThread:
    if "María" in jc.listen().strip():
        jc.jarvisTalk(choice(awaitingOrders))
        newOrder = jc.listen().strip()
        print("NEW ORDER " + newOrder)
        if any(x in newOrder for x in disconectingOrders):
            mainThread = False
            jc.jarvisTalk(choice(byeBye))

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

        elif any(order in newOrder for order in recordingOrders):
            recordConversation()

        elif "reproduce" in newOrder:
            playConversation()

        elif any(order in newOrder for order in setOrders):
            jc.setProtocol(newOrder)

        elif "hazte la loca" in newOrder:
            jc.jarvisTalk(choice(crazyMode))

        elif "apaga el ordenador" in newOrder:
            jc.jarvisTalk("Apagando el ordenador. Hasta luego")
            mainThread = False
            jc.closeComputer()
        elif "nota" in newOrder or "notas" in newOrder:
            jc.setProtocol(newOrder)
        else:
            jc.jarvisTalk(iDontUnderstand[randint(0, len(iDontUnderstand) - 1)])
    time.sleep(0.4)

