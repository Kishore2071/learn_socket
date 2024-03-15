import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    source_destination = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    final = source_destination/arp_request
    answered_list = scapy.srp(final,timeout=1,verbose=False)[0]
    
    result_list = []
    for answer in answered_list:
        result_dic= {"ip": answer[1].psrc , "mac": answer[1].hwsrc}
        result_list.append(result_dic)
    return result_list
    
def print_results(result_list):
    print("IP\t\t\tMAC Address\n----------------------------------------")
    for result in result_list:
        print(result["ip"]+"\t\t"+result["mac"])    
    
result_dic=scan("192.168.1.1/24")
print_results(result_dic)