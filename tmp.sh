#!/bin/bash

makeTmp(){
    i=0
    while read line # Todo lo capturado en el documento, será guardado en la variable line
    do
    path[$i]="$line" # Lo insertamos en la posición i del arreglo correspondiente
    ((i++)) # Aumentamos el iterador
    done < ./.path.txt # Lo repetimos hasta que no haya más elementos en el archivo
    export pathSave="${path[0]}" # Lo asignamos a las varibles globales para mayor comodidad
    export pathList="${path[1]}"
    ls "${path[0]}" > ./.log.txt # La salida del comando ls será guardado en log.txt
    #sed 's!p4!\p3\ !g' ./.log.txt > ./.finalName.txt # Cambiamos la extensión de los archivos de mp3 a mp4 del log y lo guarmos en nuevo documento|"cancion.mp4" --> "cancion.mp3" 
}

rmTmp(){
    rm "$pathSave"*.mp4
    rm ".log.txt"
    rm ".path.txt"
}