import subprocess
import optparse

# python mac_changer.py --interface eth0 --mac 00:44:44:55:77:33

def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Used to select interface")
    parser.add_option("-m","--mac",dest="new_mac",help="Used to select mac")
    return parser.parse_args()

def change_mac(interface,new_mac):
    print("Changing Mac Address "+ interface + " To " + new_mac )
    subprocess.call(["ifconfig " , interface , " down"])
    subprocess.call(["ifconfig " , interface , " hw " + " ether" + new_mac])
    subprocess.call(["ifconfig " , interface , " up"])

(options,arguments) = get_options()    
change_mac(options.interface,options.new_mac)