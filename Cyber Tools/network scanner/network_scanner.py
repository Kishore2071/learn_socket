import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    source_destination = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    final = source_destination/arp_request
    answered_list = scapy.srp(final,timeout=1,verbose=False)[0]
    scapy.ls(scapy.ARP())
    print("IP\t\t\tMAC Address\n----------------------------------------")
    for answer in answered_list:
        print(answer[1].psrc + "\t\t" + answer[1].hwsrc)
    
scan("192.168.1.1/24")