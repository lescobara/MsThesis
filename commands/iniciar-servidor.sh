# Verifica que se pase un algoritmo como parámetro
if [ -z "$1" ]; then
  echo "Uso: $0 <nombre_algoritmo>"
  exit 1
fi

# Define el algoritmo postcuántico a partir del primer parámetro
ALGORITMO=$1

#ejecutar contenedor
sudo docker run --rm -p 4433:4433 -v /home/diotallevi/tesis/server-pki/"$ALGORITMO":/opt/nginx/pki -v /home/diotallevi/tesis/server-conf:/opt/nginx/nginx-conf -v /home/diotallevi/tesis/web:/opt/nginx/html openquantumsafe/nginx
