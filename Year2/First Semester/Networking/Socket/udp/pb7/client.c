
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <arpa/inet.h>

int main() {
          int c;
          struct sockaddr_in server;


          c = socket(AF_INET, SOCK_DGRAM, 0);
         if (c < 0) {
                 printf("Eroare la crearea socketului client\n");
                 return 1;
           }
          int port;
          char IP[20];
          printf("Introduceti portul: ");
          scanf("%d",&port);
          printf("Introduceti IP: ");
          scanf("%s",IP);
          memset(&server, 0, sizeof(server));
          server.sin_port = port;
          server.sin_family = AF_INET;
          server.sin_addr.s_addr = inet_addr(IP);

                uint16_t i,l;
                char sir[120],subsir[120];
                getchar();
                printf("\n Dati sirul de caractere: ");
                fgets(sir,sizeof(sir),stdin);
                printf("\n Dati pozitia de unde incepe subsirul(i)");
                scanf("%hu",&i);
                printf("\n Dati lungimea subsirului(l): ");
                scanf("%hu",&l);
                i=htons(i);
                l=htons(l);
                int size=sizeof(server);
                sendto(c,sir,120,0,(struct sockaddr *) &server,size);
                sendto(c,&i,sizeof(i),0,(struct sockaddr *) &server,size);
                sendto(c,&l,sizeof(l),0,(struct sockaddr *) &server,size);
                i = ntohs(i);
                l = ntohs(l);
                recvfrom(c,subsir,120,0,(struct sockaddr *) &server,(socklen_t )&size);
                printf("Sir '%s' subsirul care incepe pe pozitia '%d' de lungime'%d' este: %s \n",sir,i,l,subsir);

         close(c);
}
