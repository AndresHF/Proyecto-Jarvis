import subprocess
from core.jarvisCore import *


def getNumbersInString(order):
    return [int(s) for s in order.replace("%", "").split() if s.isdigit()]


def getActualVolume():
    volAsByteArr = subprocess.Popen(
        ['pactl list sinks | grep "Volume: front" | cut -f2 -d"/" | cut -b 3-4'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        shell=True,
    )
    volToCharArr = volAsByteArr.communicate(b"' stdin")[0]
    return "".join(map(chr, volToCharArr)).strip()


def setVolume(order):

    newVol = getNumbersInString(order)[0]
    volumeOrder = "pactl -- set-sink-volume 0 "
    if "sube" in order:
        volumeOrder += "+"
    elif "baja" in order:
        volumeOrder += "-"

    volumeOrder += str(newVol).strip() + "%"
    print(volumeOrder)
    subprocess.Popen([volumeOrder], shell=True, stdout=subprocess.PIPE)
