from scapy.all import *

def packet_callback(packet):
    print(f"Packet: {packet.summary()}")

def main():
    print("Starting packet capture. Press Ctrl+C to stop.")
    try:
        sniff(prn=packet_callback, store=0, timeout=5)
    except KeyboardInterrupt:
        print("Packet capture stopped.")

main()
