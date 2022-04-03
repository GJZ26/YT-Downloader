# Youtube Downloader
YT Downloader es un aplicación escrita en Python que descarga tus canciones de YouTube en formato mp3

## Instalación
YT Downloader usa la librería de pytube para decargar música directamente a un directorio. No necesita ser compilado.

Antes de comenzar, deberás tener listo lo siguiente:
* Tener un documento txt con los links de Youtube de todas las canciones deseadas (los videos de los links deberán ser públicos para permitir su descarga)
* Las listas de canciones a descargar, deberán estar en forma de lista y sin espacios al final
* Tener la ruta de la carpeta dónde será almacenada 

Al descargar la aplicación, encontrarás un documento "runMe.sh" que es el script principal.

Se te solicitará una ruta tu playlist. Por ejemplo:
/home/user/Desktop/playlist.txt

Posteriormente se te solicitará la carpeta dónde será almacenada las canciones. Deberás ingresar una ruta como esta:
/home/user/Desktop/music

Sin barra al final de la dirección.

Finalmente espera a que tus archivos terminen de descargarse y disfruta de tu musica

## Changelog
### 1.0.1
Guarda tus documentos en una carpeta donde halla más tipos de archivos

Ahora los .mp4 se descargan en una carpeta temporal para evitar interferir o dañar otros archivos

#### Bug fix
* Ahora la conversión no se detiene si se guarda en una carpeta con archivos de múltiple extensión

### 1.0.0
Los archivos ahora son convertidos a mp3!
* Se cambió el nombre del ejecutable principal a runMe.sh
* Se ha agregado un script para eliminar los documentos temporales y archivos mp4 innecesarios

### 0.0.0a1
* Puedes asinar la ruta de un archivo de texto que contenga los links
* Puedes elegir la carpeta de destino
* Sólo descarga archivos de audio con extension .mp4
* Se añadió el documento run.sh para facilitar su ejecución