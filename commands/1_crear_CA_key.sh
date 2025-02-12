#sudo docker run -v `pwd`/tesis/server-pki/dilithium3:/opt/tmp -it openquantumsafe/curl openssl req -x509 -new -newkey rsa -keyout /opt/tmp/CA.key -out /opt/tmp/CA.crt -nodes -subj "/CN=oqstest CA" -days 365

#!/bin/bash

# Verifica que se pase un algoritmo como parámetro
if [ -z "$1" ]; then
  echo "Uso: $0 <nombre_algoritmo>"
  exit 1
fi

# Define el algoritmo postcuántico a partir del primer parámetro
ALGORITMO=$1

# Ruta base
BASE_PATH=`pwd`/tesis/server-pki

# Crea el subdirectorio para el algoritmo especificado
ALGORITMO_PATH="$BASE_PATH/$ALGORITMO"
mkdir -p "$ALGORITMO_PATH"

# Ejecuta el contenedor Docker con la ruta específica y el algoritmo
sudo docker run -v `pwd`/tesis/server-pki/"$ALGORITMO":/opt/tmp -it openquantumsafe/curl openssl req -x509 -new -newkey dilithium5 -keyout /opt/tmp/CA.key -out /opt/tmp/CA.crt -nodes -subj "/CN=oqstest CA" -days 365
