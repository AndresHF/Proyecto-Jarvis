from core.jarvisCore import *
from core.orders.system.volume import getNumbersInString


def recordConversation():
    try:
        jarvisTalk("¿Cómo quieres llamar al archivo?")
        fileName = "".join(listen().split(" ")) + ".wav"
        WAVE_OUTPUT_FILENAME = "./core/recordings/" + fileName
        print(WAVE_OUTPUT_FILENAME)
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        CHUNK = 1024
        jarvisTalk("¿Cúanto quieres que dure en segundos?")
        RECORD_SECONDS = int(getNumbersInString(listen())[0])

        jarvisTalk(
            fileName + ". Grabación de %d segundos. Comienza. Ya!" % RECORD_SECONDS
        )
        audio = pyaudio.PyAudio()

        # start Recording
        stream = audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK,
        )
        print("recording...")
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("finished recording")
        jarvisTalk("Grabación finalizada")
        # stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()

        waveFile = wave.open(WAVE_OUTPUT_FILENAME, "wb")
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b"".join(frames))
        waveFile.close()

    except:
        jarvisTalk("Error en los parámetros")


def playConversation():
    jarvisTalk("¿Qué archivo quieres reproducir?")

    fileName = "".join(listen().split(" ")) + ".wav"
    WAVE_INPUT_FILENAME = "./core/recordings/" + fileName
    try:

        CHUNK = 1024

        wf = wave.open(WAVE_INPUT_FILENAME, "rb")

        # instantiate PyAudio (1)
        p = pyaudio.PyAudio()

        # open stream (2)
        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True,
        )
        jarvisTalk("Reproduciendo grabación")
        # read data
        data = wf.readframes(CHUNK)

        # play stream (3)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)

        # stop stream (4)
        stream.stop_stream()
        stream.close()

        # close PyAudio (5)
        p.terminate()
        jarvisTalk("Reproducción finalizada")
    except:
        jarvisTalk("No existe ningún archivo llamado " + fileName)
