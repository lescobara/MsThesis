from scapy.all import rdpcap, TCP, Raw
from collections import defaultdict
import argparse

def calculate_tls_handshake_time(pcap_file):
    # Cargar el archivo .pcap
    packets = rdpcap(pcap_file)

    # Diccionario para rastrear tiempos del handshake
    handshake_times = {}

    for packet in packets:
        if TCP in packet:
            tcp_layer = packet[TCP]
            src_ip = packet[0].src
            dst_ip = packet[0].dst
            connection_id = (src_ip, dst_ip, tcp_layer.sport, tcp_layer.dport)

            if tcp_layer.flags == "S":  # Paquete SYN
                handshake_times['SYN'] = packet.time
            elif tcp_layer.flags == "SA":  # Paquete SYN-ACK
                handshake_times['SYN-ACK'] = packet.time
            elif tcp_layer.flags == "A":  # Paquete ACK
                handshake_times['ACK'] = packet.time

    print (handshake_times)

    # Calcular el tiempo de handshake para cada conexion
    syn_time = handshake_times['SYN']
    syn_ack_time = handshake_times['SYN-ACK']
    ack_time = handshake_times['ACK']
    handshake_duration = ack_time - syn_time
    print(f"Three-way handshake ({connection_id}): {handshake_duration:.6f} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze a .pcap file for TLS performance metrics.")
    parser.add_argument("pcap_file", help="Path to the .pcap file to analyze")
    args = parser.parse_args()

    calculate_tls_handshake_time(args.pcap_file)
