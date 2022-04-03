# Importamos librerías necesaria
from asyncore import read
import pytube as pyt
import os

# Solicitamos las rutas de la playlist y del lugar donde guardar el archivo
print("\nIngrese la ruta de tu playlist: ",end="")
rutaList=input()
print("Ingrese la ruta de guardado: ",end="")
rutaSave=input()
rutaSave+="/"

# Guardamos las rutas de la playlist y la carpeta para guardar en un txt para usarlo con otros códigos
print("[Guardando rutas]")
file=open("./.path.txt","w")
file.write(rutaSave+"\n")
file.write(rutaList+"\n")
file.close()

# Almacenamos los nombres de los links de la playlist en un arreglo
print("[Leyendo playlist]")
with open(rutaList,"r") as tf:
	lines = tf.read().split('\n')
lines.pop(len(lines)-1)

# Comenzamos las decargas de los archivos en mp4
print("[Inicializando descarga]")
for line in lines:
    song=pyt.YouTube(line)
    print("\nDecargando:<",line,">\n\tTítulo:",song.title,"\n\tAutor:",song.author,"\n\tDuración:",song.length,"segundos")
    song.streams.get_lowest_resolution().download(rutaSave)
    print("\t\t\t¡Listo!")
