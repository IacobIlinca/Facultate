#include <sys/types.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
int main() {
        int c, l;
        struct sockaddr_in server, client;
        int m[5][5] = {0};
        c = socket(AF_INET, SOCK_DGRAM, 0);
        if (c < 0) {
                printf("Eroare la crearea socketului client\n");
                return 1;
        }
        srand(time(0));
        memset(&server, 0, sizeof(server));
        server.sin_port = htons(2811);
        server.sin_family = AF_INET;
        server.sin_addr.s_addr = inet_addr("127.0.0.1");



        int i,j,ln,col;
        int ok;
        int nave=5, nave_adversar;
        for(i=0;i<5;i++){
                ok=0;
                while(!ok){
                        ln=rand()%5;
                        col=rand()%5;
                        if(m[ln][c]==0){
                                ok=1;
                                m[ln][c]=1;
                        }
                }
        }
        int linie, coloana;
        while(nave>0){
                for(i=0;i<5;i++,printf("\n"))
                        for(j=0;j<5;j++)
                                printf("%d", m[i][j]);
                printf("\n");
                nave=htons(nave);
                sendto(c,&nave, sizeof(nave), 0, (struct sockaddr *) &server, sizeof(server));
                nave=ntohs(nave);
                linie = rand()%5;
                coloana = rand()%5;
                printf("AM TRIMIS (%d, %d)\n", linie, coloana);
                linie=htons(linie);
                coloana=htons(coloana);
                sendto(c,&linie, sizeof(linie), 0, (struct sockaddr *) &server, sizeof(server));
                sendto(c,&coloana, sizeof(coloana), 0, (struct sockaddr *) &server, sizeof(server));
                recvfrom(c, &nave_adversar, sizeof(nave_adversar), MSG_WAITALL, (struct sockaddr *) &server,(socklen_t*) &l);
                nave_adversar=ntohs(nave_adversar);
                if(nave_adversar == 0){
                        printf("AM CASTIGAT\n");
                        break;
                }

                recvfrom(c, &linie, sizeof(linie), MSG_WAITALL, (struct sockaddr *) &server,(socklen_t*) &l);
                recvfrom(c, &coloana, sizeof(coloana), MSG_WAITALL, (struct sockaddr *) &server,(socklen_t*) &l);
                linie=ntohs(linie);
                coloana=ntohs(coloana);
                if(m[linie][coloana]){
                        m[linie][coloana]=0;
                        nave--;
                }
                if(nave==0)
                        sendto(c,&nave, sizeof(nave), 0, (struct sockaddr *) &server, sizeof(server));
        }

        close(c);
}
