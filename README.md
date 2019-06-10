# Proyecto-Jarvis
---

- [Introducción](#introducción)
- [Instalación](#instalación)
- [Despliegue](#despliegue)
- [Explicación](#explicación)
- [APIs](#apis)
- [Presentación](#presentación)
- [Enlaces de interés](#enlaces-de-interés)

---

<h2>Introducción</h2>
Este proyecto se ha realizado como <b>TFC</b> para el <b>Grado Superior de Desarrollo de Aplicaciones Web</b> en el <b>I.E.S María de Zayas y Sotomayor</b>. 
<br>
<br>
Está basado en el reconocimiento de voz para controlar el ordenador por comandos utilizando Python y linux scripting.
<h3>Instrucciones programadas:</h3>
<ul>
  <li>Búsqueda de cualquier tipo de información en Google / Wikipedia.</li>
  <li>Búsqueda de emplazamientos, restaurantes, tiendas, etc... en GoogleMaps.</li>
  <li>Reproduce bajo demanda cualquier tipo de vídeo o música de YouTube.</li>
  <li>Explica el significado de cualquier palabra preguntada.</li>
  <li>Realiza operaciones de grabación / reproducción de audios a demanda.</li>
  <li>Puede contestar sobre la temperatura de cualquier ciudad del mundo.</li>
  <li>Controlar y responder sobre el estado del volumen del sistema.</li>
  <li>Cerrar aplicaciones abiertas.</li>
  <li>Realizar búsquedas sobre ficheros en el sistema.</li>
  <li>Poner alarmas.</li>
  <li>Y lo más importante.... te cuenta chistes malos...</li>
</ul>  

Está planteado en futuras versiones añadir Inteligencia Artificial junto con chatterbot de Python.

<h2>Instalación</h2>

<h3>Prerequisitos</h3>
Es necesario ejecutar el programa en cualquier ditribución de <b><a href="https://www.linux.org/pages/download/">GNU/Linux</a></b> y tener instalado <b><a href="https://www.python.org/downloads/release/python-373/">Python3.7</a></b>

<h3>Configuración de scripts de linux</h3>
```
chmod 777 "/...mi-ruta-al-poyecto/shellScripts/alarm.sh"
chmod 777 "/...mi-ruta-al-poyecto/shellScripts/display.sh"
```
```
cp /...mi-ruta-al-poyecto/shellScripts/alarm.sh /usr/local/bin/alarm
cp /...mi-ruta-al-poyecto/shellScripts/alarm.sh /usr/local/bin/display
```
# Librerías de Python utilizadas 

<h3>speech_recognition</h3>
Responsable de transformar la voz en texto.

<h3>subprocess</h3>
Para controlar la comunicación entre el programa y la terminal.

<h3>gTTS</h3>
Librería de Google (Text To Speech), es básicamente la voz del programa.

<h3>pyaudio</h3>
Realizando operaciones de grabación y reproducción de audio.

<h3>urllib.request y bs4</h3>
Para abrir conexiones a páginas, leerlas y realizar operaciones de scrapping.
