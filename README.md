# MsThesis

Este repositorio contiene código fuente desarrollado para la recopilación y análisis de datos, orientado a experimentos y evaluaciones de desempeño de algoritmos de cifrado postcuántico desplegados en un dispositivo Edge Computing, para el desarrollo de la tesis de maestría: Implementación y evaluación de algoritmos de cifrado post cuánticos en dispositivos de Edge Computing desplegados en una red de cómputo que emplea el protocolo TCP para fortalecer la seguridad en la capa de transporte. Incluye scripts en Python para análisis estadístico y de tráfico (pcap) y un conjunto de scripts en Bash para la configuración y generación de datos, así como para iniciar servicios y herramientas relacionadas.

## Contenido del Repositorio

### Archivos Python

- **anova.py**\
  Este script realiza un análisis de varianza (ANOVA) de un solo factor.\
  **Entradas:**

  - Recibe como argumento el nombre de un archivo CSV (con valores separados por tabuladores) que contenga los datos a analizar.\
    **Ejecución:**

  ```bash
  python anova.py <archivo_datos.csv>
  ```

- **generate-data.py**\
  Genera datos simulados de sensores y escribe un archivo CSV llamado `datos_sensores.csv` de aproximadamente 2 MB.\
  **Ejecución:**

  ```bash
  python generate-data.py
  ```

- **pcap\_analysis2.py**\
  Analiza archivos `.pcap` para evaluar diversos parámetros de rendimiento del tráfico de red.\
  **Entradas:**

  - Se requiere la ruta a un directorio que contenga archivos `.pcap`.\
    **Ejecución:**

  ```bash
  python pcap_analysis2.py <directorio_de_pcaps>
  ```

- **tls\_analysis3.py**\
  Analiza un archivo `.pcap` para calcular el tiempo del handshake TLS de una conexión.\
  **Entradas:**

  - Se requiere la ruta a un único archivo `.pcap`.\
    **Ejecución:**

  ```bash
  python tls_analysis3.py <archivo.pcap>
  ```

### Scripts en Bash (Carpeta `commands`)

- **1\_crear\_CA\_key.sh**\
  Crea la clave de la Autoridad Certificadora (CA).

- **2\_crear\_server\_key\_algoritmo.sh**\
  Genera la clave privada del servidor utilizando un algoritmo específico.

- **3\_crear\_server\_certificate.sh**\
  Emite el certificado del servidor, firmándolo con la CA creada previamente.

- **get\_data.sh**\
  Script para la recopilación o descarga de datos.

- **iniciar-servidor-sencillo.sh**\
  Inicia un servidor básico.

- **iniciar-servidor.sh**\
  Inicia el servidor con configuraciones avanzadas.

- **iniciar\_wireshark.sh**\
  Lanza Wireshark para capturar tráfico.

## Requisitos

- **Python 3.x** con las bibliotecas:

  - `pandas`
  - `scipy`
  - `scapy`
  - `statistics` (módulo estándar)
  - `argparse` (módulo estándar)

- **Entorno Bash** para ejecutar los scripts en la carpeta `commands`.

- **Wireshark** (opcional) para análisis de tráfico.

## Cómo Ejecutar

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/lescobara/MsThesis.git
   cd MsThesis
   ```

2. **Instalar dependencias de Python:**

   ```bash
   pip install pandas scipy scapy
   ```

3. **Ejecutar los scripts según la tarea deseada:**

   ```bash
   python generate-data.py
   python anova.py <archivo_datos.csv>
   python pcap_analysis2.py <directorio_de_pcaps>
   python tls_analysis3.py <archivo.pcap>
   ```

   Para scripts en `commands`:

   ```bash
   cd commands
   ./1_crear_CA_key.sh
   ```

## Licencia

Este proyecto se distribuye bajo la licencia [GPL-3.0](LICENSE).


