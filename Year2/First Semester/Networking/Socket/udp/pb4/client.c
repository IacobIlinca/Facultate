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
        int c,l;
        char buffer[101];
        struct sockaddr_in server;
        uint16_t nr, i, k;


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
        recvfrom(c,buffer,sizeof(buffer), MSG_WAITALL, (struct sockaddr*) &server,(socklen_t *)&l);
        printf("Sirul oglindit este:%s",buffer);

  close(c);
}
