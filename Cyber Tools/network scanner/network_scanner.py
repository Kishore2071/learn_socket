import scapy.all as scapy
import optparse

def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-r","--range",dest="range",help="Used to select range")
    (options,arguments) = parser.parse_args()
    if not options.range:
        parser.error("range not specified! use --help to get more info")
    else:
        return options

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

options = get_options()    
    
result_dic=scan(options.range)
print_results(result_dic)