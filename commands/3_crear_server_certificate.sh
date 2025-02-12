# Verifica que se pase un algoritmo como parámetro
if [ -z "$1" ]; then
  echo "Uso: $0 <nombre_algoritmo>"
  exit 1
fi

# Define el algoritmo postcuántico a partir del primer parámetro
ALGORITMO=$1

sudo docker run -v `pwd`/tesis/server-pki/"$ALGORITMO":/opt/tmp -it openquantumsafe/curl openssl x509 -req -in /opt/tmp/server.csr -out /opt/tmp/server.crt -CA /opt/tmp/CA.crt -CAkey /opt/tmp/CA.key -CAcreateserial -days 365
