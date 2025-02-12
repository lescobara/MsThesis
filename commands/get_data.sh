#!/bin/bash

# Verificar el parametro
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Uso: $0 nombre_algoritmo nombre_directorio_local"
    exit 1
fi

# Almacenar el parametro dentro de una variable
nombre_algoritmo=$1
nombre_directorio_local=$2

# Ruta al archivo que deseas copiar
archivo_a_copiar="/home/diotallevi/supercop-20240425/bench/tesis/data"

# Datos del servidor remoto
servidor="x.x.x.x"
puerto="xx"
ruta_remota_base="xxxxx"
usuario="xxxxxx"
password="xxxxx"

# Ruta completa del directorio remoto
ruta_remota="${ruta_remota_base}${nombre_algoritmo}/"

expect << DONE
    spawn ssh -p "$puerto" -o StrictHostKeyChecking=no ${usuario}@${servidor} "mkdir -p ${ruta_remota}"
    expect "password:"
    send "$password\r"
    expect eof
DONE


# Ejecutar el comando 8 veces
for i in {1..8}
do
    # Ejecutar el comando original
    ./do-part "$nombre_directorio_local" "$nombre_algoritmo"

    # Copiar el archivo al servidor remoto usando scp
    expect << DONE
        spawn scp -P "$puerto" -o StrictHostKeyChecking=no "$archivo_a_copiar" ${usuario}@${servidor}:${ruta_remota}
        expect "password:"
        send "$password\r"
        expect eof
DONE
   # Agregar informacion al archivo en el servidor remoto
    fecha_hora=$(date "+%Y-%m-%d_%H-%M")
    nuevo_nombre="data-${fecha_hora}-${nombre_algoritmo}"
    expect << DONE
        spawn ssh -p "$puerto" -o StrictHostKeyChecking=no ${usuario}@${servidor} "mv ${ruta_remota}data ${ruta_remota}${nuevo_nombre}"
        expect "password:"
        send "$password\r"
        expect eof
DONE
done

echo "Comando y copia ejecutados 8 veces con el algoritmo: $nombre_algoritmo"
