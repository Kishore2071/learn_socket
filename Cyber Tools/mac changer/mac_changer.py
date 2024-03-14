import subprocess
import optparse
import re

# python mac_changer.py --interface eth0 --mac 00:44:44:55:77:33

def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Used to select interface")
    parser.add_option("-m","--mac",dest="new_mac",help="Used to select mac")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("interface not specified! use --help to get more info")
    elif not options.new_mac:
        parser.error("mac id not specified! use --help to get more info")
    else:
        return options

def change_mac(interface,new_mac):
    print("Changing Mac Address "+ interface + " To " + new_mac )
    subprocess.call(["ifconfig " , interface , " down"])
    subprocess.call(["ifconfig " , interface , " hw " + " ether" + new_mac])
    subprocess.call(["ifconfig " , interface , " up"])

def get_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig",interface])
    filter_result=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    if filter_result:
        return filter_result.group(0)
    else:
        print("Mac Address Not found")

options = get_options()    
mac_address_filter_results = get_mac_address(options.interface)
print("Current Mac Address = " + str(mac_address_filter_results))

change_mac(options.interface,options.new_mac)

if mac_address_filter_results==options.new_mac:
    print("Mac Address Changed to: "+ mac_address_filter_results)
else:
    print("Mac Address Not Changed")