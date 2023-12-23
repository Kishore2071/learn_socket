#include<stdio.h>
#include<pcap.h>   // To invoke the libpcap library and use its functions 

int main(int argc,char *argv[]){

    char error[PCAP_ERRBUF_SIZE];
    pcap_if_t *interfaces, *temp;
    int i=0;

    if(pcap_findalldevs(&interfaces, error) == -1){
        printf("Cannot acquire the Devices\n");
        return -1;
    }

    printf("The available interfaces are: \n");

    for(temp=interfaces;temp;temp=temp->next){
        printf("#%d: %s\n",++i,temp->name);
    }

    return 0;
}