#include <unistd.h>
#include <unistd.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>

int main() {
        int i,c,l;
        char buffer[101],x;
        struct sockaddr_in server;
        uint16_t k,poz;


        c = socket(AF_INET, SOCK_DGRAM, 0);
        if (c < 0) {
                printf("Eroare la crearea socketului client\n");
                return 1;
        }

        memset(&server, 0, sizeof(server));
        server.sin_port = htons(2105);
        server.sin_family = AF_INET;
        server.sin_addr.s_addr = inet_addr("127.0.0.1");

        printf("Sirul=");
        gets(buffer);
        sendto(c, buffer, sizeof(buffer), 0, (struct sockaddr *) &server, sizeof(server));
        printf("Dati caracterul:");
        scanf("%c",&x);
        sendto(c,&x,sizeof(x),0,(struct sockaddr *)&server,sizeof(server));
        recvfrom(c,&k,sizeof(k), MSG_WAITALL, (struct sockaddr*) &server,(socklen_t *)&l);
        k=ntohs(k);
        printf("Pozitiile pe care se afla caracterul '%c' sunt:",x);
        for(i=0;i<k;i++)
        {
                recvfrom(c,&poz,sizeof(poz), MSG_WAITALL, (struct sockaddr*) &server,(socklen_t *)&l);
                poz=ntohs(poz);
                printf("%hu ",poz);
        }

  close(c);
}
