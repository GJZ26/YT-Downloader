#!/bin/bash

# Este programa está hecho con fines de satisfacer mis necesidades domésticas
# Si les sirve, puede usarla sin ninguna restricción

# Este ejecutable corre los programas de forma secuencial

# Importamos el script tmp.sh
source tmp.sh 

clear
echo -e ".-.-.-.-.-.-. YT Downloader 1.0.0 .-.-.-.-.-.-.\n"

# Corremos el programas script que decarga los archivos mp4
/usr/bin/python3 ./dowloader.py

# Corremos el script que nos crea los archivos temporales
echo -e "\n[Creando registro de decargas]"
makeTmp

# Corremos el programa que convertirá los archivos mp4 descargados en mp3
/usr/bin/python3 ./conversor.py

#Eliminamos archivos temporales y formatos de mp4 innecesarios
echo "[Limpiando archivos temporales]"
rmTmp

echo -e "\nCerrando programa..."
read -t 10 -p "Presione enter para hacerlo de inmediato"
