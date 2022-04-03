from asyncore import read
import moviepy.editor as mp

# Del archivo path.txt guardamos las rutas en arreglo
# Path [0] = Ruta dónde se encuentran los archivos decargados
# Path [1] = Ruta dónde se encuentra la playlist
print("[Leyendo rutas de acceso]")
with open ("./.path.txt","r") as qw:
    path = qw.read().split('\n')
path.pop(len(path)-1)

# Guardamos la lista de las caciones decargadas en arreglo
print("[Leyendo lista de descarga]")
with open ("./.log.txt","r") as er:
    songSource = er.read().split('\n')
songSource.pop(len(songSource)-1)

# Realizamos la conversion por los documentos contenidos en log.txt
print("\n[Inicializando conversión]")
for i in range(len(songSource)):
    source1=path[0]+songSource[i]
    x=songSource[i]
    source2=path[0]+x.replace("mp4","mp3")
    print("Convirtiendo: ",x)
    clip = mp.VideoFileClip(source1)
    clip.audio.write_audiofile(source2)
    
print("\n[Conversión finalizada]")
