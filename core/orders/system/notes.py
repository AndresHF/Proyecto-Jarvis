import core.jarvisCore as jc
from core.orders.constants import *
import subprocess
from random import choice
from core.orders.web_operations.scraping import *

noteAsnwers = {"leer": "leída", "actualizar": "actualizada", "borrar": "borrada"}


def notesOperations(order):
    if any(x in order for x in notesAddConstants):
        addNewNote()
        jc.jarvisTalk("Nota finalizada")
    elif any(x in order for x in knowNotes):
        enumerateNotes()
    elif any(x in order for x in noteContent):
        doThingsInNotes(order, "leer")
    elif any(x in order for x in modifyNote):
        doThingsInNotes(order, "actualizar")
    elif any(x in order for x in delteNote):
        doThingsInNotes(order, "borrar")


def doThingsInNotes(order, mode):

    allNotes = getAllNotes()
    if len(allNotes) > 0:
        fileName = "".join(order.split("nota")[1]).strip()
        if len(fileName) == 0:
            jc.jarvisTalk("¿Cuál de ellas?")
            fileName = "".join(jc.listen().lower().split(" ")) + ".txt"
        else:
            fileName = "".join(fileName.split(" ")) + ".txt"

        if fileName.replace("txt", "") not in getAllNotes():
            jc.jarvisTalk("No he encontrado la nota " + fileName + ".")
            jc.jarvisTalk("¿Quieres saber cuáles tienes?")
            answer = jc.listen()
            if answer == "sí":
                enumerateNotes()
                jc.jarvisTalk("¿Qué nota quieres " + mode + "?")
                doThingsInNotes("nota " + jc.listen(), mode)

        else:
            noteSwitchOperato(fileName, mode)
    else:
        jc.jarvisTalk("No tienes notas")


def noteSwitchOperato(fileName, mode):
    try:
        if mode == "leer":
            noteContent = getShellOutput("cat ./core/notes/" + fileName)
            jc.jarvisTalk(noteContent)
        elif mode == "actualizar":
            addRowsToNote(fileName)
        elif mode == "borrar":
            subprocess.call(["rm ./core/notes/" + fileName], shell=True)
        jc.jarvisTalk("Nota" + noteAsnwers[mode])

    except:
        jc.jarvisTalk("Error en los parámetros")


def enumerateNotes():
    allNotes = getAllNotes()
    if len(allNotes) > 0:
        jc.jarvisTalk("Tus notas son:")
        jc.jarvisTalk(allNotes)
    else:
        jc.jarvisTalk("No existen notas")


def getAllNotes():
    try:
        return getShellOutput("ls ./core/notes/").replace("txt", "")
    except:
        jc.jarvisTalk("No existen notas")
        return ""


def getShellOutput(cmd):
    popen = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    return "".join(map(chr, popen.communicate()[0]))


def deleteNote():

    answer = ""
    while len(answer) == 0:
        jc.jarvisTalk("¿Qué nota quieres eliminar?")


def addNewNote():
    try:

        fileName = ""

        while len(fileName) == 0:
            jc.jarvisTalk("¿Cómo quieres llamar a la nota?")
            fileName = jc.listen().lower()
            if len(fileName) == 0:
                jc.jarvisTalk("No has dicho nada")
        fileName = "".join(fileName.split(" ")) + ".txt"
        jc.jarvisTalk(
            "Nombre establecido. " + fileName.replace("txt", "") + ". Creando archivo."
        )
        subprocess.call(["touch ./core/notes/" + fileName], shell=True)
        jc.jarvisTalk("Archivo creado.")
        addRowsToNote(fileName)

    except:
        jc.jarvisTalk("Ooops. Me he quedado pillada")


def addRowsToNote(fileName):
    jc.jarvisTalk("Comienzo a tomar notas. Para finalizar di: Finalizar nota")
    newLine = ""
    while newLine != "finalizar nota":
        newLine = makeTrans(jc.listen())
        if len(newLine) > 0 and newLine != "finalizar nota":
            subprocess.call(
                ["echo '" + newLine + ".' >> ./core/notes/" + fileName], shell=True
            )
            jc.jarvisTalk(choice(afirmativeNoteWrited))
        elif len(newLine) == 0:
            jc.jarvisTalk("No has dicho nada")

