import subprocess

interface = input("Enter Interfaces: ")
new_mac = input("Enter New mac: ")

print("Changing Mac Address "+ interface + " To " + new_mac )

subprocess.call("ifconfig " + interface + " down",shell=True )
subprocess.call("ifconfig " + interface + " hw ether" + new_mac,shell=True )
subprocess.call("ifconfig " + interface + " up",shell=True )

