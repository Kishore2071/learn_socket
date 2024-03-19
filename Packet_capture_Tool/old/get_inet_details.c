#include <stdio.h>
#include <stdlib.h>
#include <pcap.h> // To invoke the libpcap library and use its functions.
#include <errno.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(){
	char *device_name, *net_addr, *net_mask;
	int rcode;
	char error[PCAP_ERRBUF_SIZE];
	
	bpf_u_int32 net_addr_int, net_mask_int; //IP address as unsined 32bit integer
	struct in_addr addr;
	
	//Asks pcap to give us a valid eth based device to sniff on it
	device_name = pcap_lookupdev(error);
	if(device_name == NULL){
		printf("%s\n", error);
		return -1;
	} else {
		printf("Device: %s\n", device_name);
	}
	
	//With the device in place, acquire the IP address and the Subnet Mask.
	rcode = pcap_lookupnet(device_name, &net_addr_int, &net_mask_int, error);
	if(rcode == -1){
		printf("%s\n", error);
		return -1;
	}
	
	//Convert the 32 bit int of IP and Mask into human readable form. 
	addr.s_addr = net_addr_int;
	net_addr = inet_ntoa(addr);
	
	if(net_addr == NULL){
		printf("inet_ntoa: Error converting IP\n");
		return -1;
	} else {
		printf("Net: %s\n", net_addr);
	}
	
	addr.s_addr = net_mask_int;
	net_mask = inet_ntoa(addr);
	
	if(net_mask == NULL){
		printf("inet_ntoa: Error converting Netmask\n");
		return -1;
	} else {
		printf("Mask: %s\n", net_mask);
	}
	
	return 0;
}
	
	
	
	
	
	 
