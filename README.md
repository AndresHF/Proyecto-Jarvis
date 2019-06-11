# Proyecto-Jarvis
---

- [Introducción](#introducción)
- [Instalación](#instalación)
- [Comandos](#comandos)
- [Documentación](#documentación)

---

<h2>Introducción</h2>
Este proyecto se ha realizado como <b>TFC</b> para el <b>Grado Superior de Desarrollo de Aplicaciones Web</b> en el <b><a href="http://ies.mariadezayas.majadahonda.educa.madrid.org/Joomla/">I.E.S María de Zayas y Sotomayor</a></b>. 
<br>
<br>
Está basado en el reconocimiento de voz para controlar el ordenador por comandos utilizando Python y linux scripting.
<h3>Instrucciones programadas:</h3>
<ul>
  <li>Búsqueda de cualquier tipo de información en Google / Wikipedia.</li>
  <li>Búsqueda de emplazamientos, restaurantes, tiendas, etc... en GoogleMaps.</li>
  <li>Establece rutas en GoogleMaps pudiendo añadir múltiples destinos</li>
  <li>Reproduce bajo demanda cualquier tipo de vídeo o música de YouTube.</li>
  <li>Explica el significado de cualquier palabra preguntada.</li>
  <li>Realiza operaciones de grabación / reproducción de audios a demanda.</li>
  <li>Puede contestar sobre la temperatura de cualquier ciudad del mundo.</li>
  <li>Controla y responde sobre el estado del volumen del sistema.</li>
  <li>Cierra aplicaciones abiertas.</li>
  <li>Realiza búsquedas sobre ficheros en el sistema.</li>
  <li>Pone alarmas.</li>
  <li>Y lo más importante.... te cuenta chistes malos...</li>
</ul>  

Está planteado en futuras versiones añadir Inteligencia Artificial junto con chatterbot de Python.

<h2>Instalación</h2>

<h3>Prerequisitos</h3>
Es necesario ejecutar el programa en cualquier ditribución de <b><a href="https://www.linux.org/pages/download/">GNU/Linux</a></b> y tener instalado <b><a href="https://www.python.org/downloads/release/python-373/">Python3.7</a></b>.
<br>
Será necesario también tener instalado Google-Chrome, wmctrl, pactl, cvlc y xterm.
<br>
Descarga el repositorio:

```
git clone https://github.com/AndresHF/Proyecto-Jarvis.git
```

<h3>Configuración de scripts de linux</h3>

```
chmod 777 "/...mi-ruta-al-poyecto/shellScripts/alarm.sh"
```

```
chmod 777 "/...mi-ruta-al-poyecto/shellScripts/display.sh"
```

```
cp /...mi-ruta-al-poyecto/shellScripts/alarm.sh /usr/local/bin/alarm
```
```
cp /...mi-ruta-al-poyecto/shellScripts/alarm.sh /usr/local/bin/display
```
<h3>Librerías de Python</h3>
Para instalar las dependencias sitúate en la carpeta raíz del proyecyo.
<br>
Si no tienes pip3.7:

```
python3.7 -m pip install pip
```

<h4><a href="https://pypi.org/project/SpeechRecognition/">speech_recognition</a></h4>
Responsable de transformar la voz en texto.

```
pip3.7 install speech_recognition
```

<h4><a href="https://pypi.org/project/gTTS/">gTTS</a></h4>
Librería de Google (Text To Speech), es básicamente la voz del programa.

```
pip3.7 install gTTS
```

<h4><a href="https://pypi.org/project/PyAudio/">PyAudio</a></h4>
Realizando operaciones de grabación y reproducción de audio.

```
pip3.7 install pyaudio
```

<h4>urllib.request y <a href="https://pypi.org/project/beautifulsoup4/">bs4</a></h4>
Para abrir conexiones a páginas, leerlas y realizar operaciones de scrapping.

```
pip3.7 install beautifulsoup4
```

<h4>Si has seguido todos los pasos</h4>
Sitúate en la raíz del proyecto y ejecuta el programa:

```
python3.7 jarvis.py
```

<h3>Comandos</h3>

Para activar a María, simplemente menciona su nombre. Una vez contesta, puedes ordenar las siguientes instrucciones:

<ul>
  <li>Busca [orden de parámetros (ej: ropa de oferta)]</li>
  <li>Busca en Wikipedia [orden de parámetros (ej: Mahatma Gandhi)]</li>
  <li>Busca en maps [orden de parámetros (ej: restaurantes cerca de Novelda Alicante)]</li>
  <li>Busca rutas: [origen (ej: Madrid), destino(ej: Frankfurt Alemania), más destinos | "finaliza"]</li>
  <li>Busca en el sistema [orden de parámetros (ej: descargas)]</li>
  <li>Pon [orden de parámetros (ej: documental sobre la informática)]</li>
  <li>Qué es/son [el/la | los/las | etc..] [orden de parámetros (ej: roedor)]</li>
  <li>Graba la conversación</li>
  <li>Reproduce una conversación</li>
  <li>Qué [tiempo / temperatura] hace en [orden de parámetros (ej: Río de Janeiro)] </li>
  <li>Pon el volumen al [orden de parámetros (ej: 50)][% | puntos | ""]</li>
  <li>[Sube / baja] el volumen [orden de parámetros (ej: 10)][% | puntos | ""]</li>
  <li>Dime el estado actual del volumen</li>
  <li>Cierra [Chrome | code | etc]</li>
  <li>Pon una alarma a las [orden de parámetros (ej: 17:30 | 17)]</li>
  <li>Cuéntame un chiste</li>
  <li>Quién eres</li>
  <li>Cuál es tu propósito</li>
</ul> 

<h3>Documentación</h3>
<h2>Aprendiendo Python</h2>
<ul>
  <li><a href="https://docs.python.org/3/">Python 3.7.3 documentation</a></li>
  <li><a href="https://www.pythoncentral.io/">pythoncentral.io</a></li>
</ul>
<h2>Teoría</h2>
<ul>
  <li><a href="https://www.lumenvox.com/espanol/resources/tips/historyOfSpeechRecognition.aspx">Historia del reconocimiento de voz 1</a></li>
  <li><a href="">Historia del reconocimiento de voz 2</a></li>
  <li><a href="https://es.wikipedia.org/wiki/Reconocimiento_del_habla">Características del reconocimiento de voz</a></li>
  <li><a href="http://director-it.com/index.php/es/ssoluciones/servicio-de-voz/acd,-call-center,-pabx/178-asr-reconocedor-de-voz.html">¿Cómo funciona el roconocimiento de voz?</a></li>
  <li><a href="https://es.wikipedia.org/wiki/Modelo_oculto_de_M%C3%A1rkov">Modelo oculto de Markov</a></li>
</ul>
<h2>Dependencias</h2>
<ul>
  <li><a href="https://realpython.com/python-speech-recognition/">speech_recognition</a></li>
  <li><a href="https://gtts.readthedocs.io/en/v2.0.0/">gTTS</a></li>
  <li><a href="https://people.csail.mit.edu/hubert/pyaudio/docs/">PyAudio</a></li>
  <li><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">Beautiful Soup</a></li>
</ul>
