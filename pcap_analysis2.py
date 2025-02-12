from scapy.all import rdpcap, TCP
import statistics
import os
import argparse

def calcular_latencia(packets):
    tiempos = []
    inicio = None

    for pkt in packets:
        if 'TCP' in pkt:
            if pkt[TCP].flags == 'S':  # Sincronización de conexión
                inicio = pkt.time
            elif pkt[TCP].flags == 'A' and inicio is not None:  # Reconocimiento
                fin = pkt.time
                tiempos.append(fin - inicio)
                inicio = None

    return statistics.mean(tiempos) if tiempos else None

def contar_retransmisiones(packets):
    seen_seq = set()
    retransmisiones = 0

    for pkt in packets:
        if TCP in pkt:
            seq = pkt[TCP].seq
            if seq in seen_seq:
                retransmisiones += 1
            else:
                seen_seq.add(seq)

    return retransmisiones

def calcular_tamano_promedio(packets):
    total_size = sum(len(pkt) for pkt in packets)
    return total_size / len(packets) if packets else 0

def contar_paquetes_y_tiempo(packets):
    num_paquetes = len(packets)

    if num_paquetes > 0:
        tiempo_inicio = packets[0].time
        tiempo_fin = packets[-1].time
        tiempo_total = tiempo_fin - tiempo_inicio
        return num_paquetes, tiempo_total
    return 0, 0

def calculate_tls_handshake_time(packets):
    handshake_durations = []
    handshake_times = {}
    for packet in packets:
        if TCP in packet:
            tcp_layer = packet[TCP]
            src_ip = packet[0].src
            dst_ip = packet[0].dst
            connection_id = (src_ip, dst_ip, tcp_layer.sport, tcp_layer.dport)

            #handshake_times = {}
            if tcp_layer.flags == "S":  # Paquete SYN
                handshake_times['SYN'] = packet.time
            elif tcp_layer.flags == "SA":  # Paquete SYN-ACK
                handshake_times['SYN-ACK'] = packet.time
            elif tcp_layer.flags == "A":  # Paquete ACK
                handshake_times['ACK'] = packet.time

            #print (handshake_times)

            if 'SYN' in handshake_times and 'SYN-ACK' in handshake_times and 'ACK' in handshake_times:
                syn_time = handshake_times['SYN']
                syn_ack_time = handshake_times['SYN-ACK']
                ack_time = handshake_times['ACK']
                handshake_duration = ack_time - syn_time
                handshake_durations.append(handshake_duration)

    return statistics.mean(handshake_durations) if handshake_durations else None

# Función principal
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analizar archivos .pcap para evaluar rendimiento de tráfico.")
    parser.add_argument("pcap_directory", help="Ruta del directorio que contiene los archivos .pcap")
    args = parser.parse_args()

    latencias = []
    retransmisiones_totales = []
    tamanos_promedio = []
    paquetes_totales = []
    tiempos_totales = []
    handshake_times = []

    # Iterar sobre cada archivo .pcap en el directorio
    for filename in os.listdir(args.pcap_directory):
        if filename.endswith(".pcap"):
            pcap_path = os.path.join(args.pcap_directory, filename)
            print(f"Analizando archivo: {filename}")

            packets = rdpcap(pcap_path)

            latencia = calcular_latencia(packets)
            if latencia is not None:
                latencias.append(latencia)

            retransmisiones_totales.append(contar_retransmisiones(packets))
            tamanos_promedio.append(calcular_tamano_promedio(packets))

            num_paquetes, tiempo_total = contar_paquetes_y_tiempo(packets)
            paquetes_totales.append(num_paquetes)
            tiempos_totales.append(tiempo_total)

            handshake_time = calculate_tls_handshake_time(packets)
            if handshake_time is not None:
                handshake_times.append(handshake_time)

    # Calcular promedios finales con redondeo
    if latencias:
        print("Promedio global de latencia:", round(statistics.mean(latencias), 4))
    if retransmisiones_totales:
        print("Promedio global de retransmisiones:", round(statistics.mean(retransmisiones_totales)))
    if tamanos_promedio:
        print("Promedio global de tamaño de paquetes:", round(statistics.mean(tamanos_promedio), 4))
    if paquetes_totales and tiempos_totales:
        print("Promedio global de cantidad de paquetes:", round(statistics.mean(paquetes_totales)))
        print("Promedio global de tiempo total de transmisión:", round(statistics.mean(tiempos_totales), 4))
    if handshake_times:
        print("Promedio global de tiempo de handshake TLS:", round(statistics.mean(handshake_times), 6))
