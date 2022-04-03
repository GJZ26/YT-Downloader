# Youtube Downloader
YT Downloader es un aplicación sencilla que descarga tus canciones de YT directo a mp3

## Instalación
Downloader usa la librería de pytube para decargar música directamente a un directorio seleccionado. No necesita ser compilado.

Antes de comenzar, deberás tener listo esto:
* Tener un documento txt con los links de Youtube de todas las canciones deseadas (estos links deberán ser públicos para permitir su descarga)
* Las listas de canciones a descargar, deberá ir en forma de lista y sin espacioal final
* Tener la ruta de la carpeta dónde será almacenada 

Al descargar la aplicación, encontrarás un documento "run.sh" que es el script principal.

Se te solicitará una ruta tu playlist. Por ejemplo:
/home/user/Desktop/playlist.txt

Posteriormente se te solicitará la carpeta dónde será almacenada las canciones. Deberás ingresar una ruta como esta:
/home/user/Desktop/music

Sin barra al final de la dirección.

Finalmente espera a que tus archivos terminen de descargarse y disfruta de tu musica

## Changelog
### 1.0.0
Los archivos ahora son cconvertidos a mp3!
* Se cambió el nombre del ejecutable principal a runMe.sh
* Se ha agregado un script para eliminar los documentos temporales y archivos mp4 innecesario

### 0.0.0a1
* Puedes asinar la ruta de un archivo de texto dónde contenga los links
* Puedes elegir la carpeta de destino
* Sólo descarga archivos de audio con extension .mp4
* Se añadió el documento run.sh para facilitar su ejecución
