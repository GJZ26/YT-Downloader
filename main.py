from asyncore import read
import pytube as pyt
import os

print("-------YT Downloader V0.0.0a1-------")
print("\nIngrese la ruta de tu playlist: ",end="")
rutaList=input()
print("Ingrese la ruta de guardado: ",end="")
rutaSave=input()
rutaSave+="/"


print("\nLeyendo Playlist...")
with open(rutaList,"r") as tf:
	lines = tf.read().split('\n')
lines.pop(len(lines)-1)

print("/n Inicializando descarga...")
for line in lines:
    song=pyt.YouTube(line)
    print("\nDecargando:<",line,">\n\tTítulo:",song.title,"\n\tAutor:",song.author,"\n\tDuración:",song.length,"segundos")
    song.streams.get_audio_only().download(rutaSave)
    print("\n¡Listo!")


print("\n\n- - - Fin del programa - - -")