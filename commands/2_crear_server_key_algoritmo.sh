# Verifica que se pase un algoritmo como parámetro
if [ -z "$1" ]; then
  echo "Uso: $0 <nombre_algoritmo>"
  exit 1
fi

# Define el algoritmo postcuántico a partir del primer parámetro
ALGORITMO=$1

#Ejecuta el contenedor
sudo docker run -v `pwd`/tesis/server-pki/"$ALGORITMO":/opt/tmp -it openquantumsafe/curl openssl req -new -newkey "$ALGORITMO" -keyout /opt/tmp/server.key -out /opt/tmp/server.csr -nodes -subj "/CN=nginx.server.tesis.org"
