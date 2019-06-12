import subprocess
from core.jarvisCore import *
from core.orders.system.notes import getShellOutput


def getNumbersInString(order):
    return [int(s) for s in order.replace("%", "").split() if s.isdigit()]


def getActualVolume():
    return getShellOutput(
        'pactl list sinks | grep "Volume: front" | cut -f2 -d"/" | cut -b 3-4'
    )


def setVolume(order):

    newVol = getNumbersInString(order)[0]
    volumeOrder = "pactl -- set-sink-volume 0 "
    if "sube" in order:
        volumeOrder += "+"
    elif "baja" in order:
        volumeOrder += "-"

    volumeOrder += str(newVol).strip() + "%"
    print(volumeOrder)
    subprocess.call([volumeOrder], shell=True)

