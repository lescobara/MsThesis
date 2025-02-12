import csv
import random
from datetime import datetime, timedelta

# Nombre del archivo y tamaño deseado en MB
nombre_archivo = 'datos_sensores.csv'
tamano_deseado = 2 * 1024 * 1024  # 2 MB en bytes

# Generar datos de ejemplo
def generar_datos_sensores(num_registros):
    datos = []
    for _ in range(num_registros):
        id_sensor = f"S{random.randint(1000, 9999)}"
        ubicacion = random.choice(["Edificio A", "Edificio B", "Exteriores", "Sótano"])
        fecha_hora = datetime.now() - timedelta(minutes=random.randint(0, 60*24))
        temperatura = round(random.uniform(15.0, 30.0), 2)
        humedad = round(random.uniform(30.0, 80.0), 2)
        nivel_bateria = round(random.uniform(10.0, 100.0), 2)
        
        datos.append([
            id_sensor,
            ubicacion,
            fecha_hora.strftime("%Y-%m-%d %H:%M:%S"),
            temperatura,
            humedad,
            nivel_bateria
        ])
    return datos

# Escribir los datos en el archivo .csv hasta alcanzar el tamaño deseado
with open(nombre_archivo, mode='w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    # Escribir encabezados
    writer.writerow(["ID Sensor", "Ubicacionn", "Fecha y Hora", "Temperatura (C)", "Humedad (%)", "Nivel de Bateria (%)"])
    
    # Agregar registros hasta alcanzar el tamaño deseado
    while archivo_csv.tell() < tamano_deseado:
        # Generar un lote de registros
        registros = generar_datos_sensores(500)
        # Escribir registros en el archivo
        writer.writerows(registros)

print(f"Archivo '{nombre_archivo}' generado(aprox. 2 MB)")
