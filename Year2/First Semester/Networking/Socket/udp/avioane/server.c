#include <sys/types.h>
#include <unistd.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
int main() {
        int s,l;
        struct sockaddr_in server, client;
        int m[5][5] = {0};
        s = socket(AF_INET, SOCK_DGRAM, 0);
        if (s < 0) {
                printf("Eroare la crearea socketului server\n");
                return 1;
        }

        memset(&server, 0, sizeof(server));
        server.sin_port = htons(2811);
        server.sin_family = AF_INET;
        server.sin_addr.s_addr = INADDR_ANY;

        if (bind(s, (struct sockaddr *) &server, sizeof(server)) < 0) {
                printf("Eroare la bind\n");
                return 1;
        }

        l = sizeof(client);
        memset(&client, 0, sizeof(client));
        srand(time(0));
        int i,j,ln,c;
        int ok;
        int nave=5, nave_adversar;
        for(i=0;i<5;i++){
                ok=0;
                while(!ok){
                        ln=rand()%5;
                        c=rand()%5;
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
        recvfrom(s, &nave_adversar, sizeof(nave_adversar), MSG_WAITALL, (struct sockaddr *) &client,(socklen_t*) &l);
        nave_adversar=ntohs(nave_adversar);
        if(nave_adversar == 0){
                printf("AM CASTIGAT\n");
                break;
        }
        recvfrom(s, &linie, sizeof(linie), MSG_WAITALL, (struct sockaddr *) &client,(socklen_t*) &l);
        recvfrom(s, &coloana, sizeof(coloana), MSG_WAITALL, (struct sockaddr *) &client,(socklen_t*) &l);
        linie=ntohs(linie);
        coloana=ntohs(coloana);
        if(m[linie][coloana]){
                m[linie][coloana]=0;
                nave--;
        }
        nave=htons(nave);
        sendto(s,&nave, sizeof(nave), 0, (struct sockaddr *) &client, sizeof(client));
        nave=ntohs(nave);
        linie = rand()%5;
        coloana = rand()%5;
        printf("AM TRIMIS (%d, %d)\n", linie, coloana);
        linie=htons(linie);
        coloana=htons(coloana);
        sendto(s,&linie, sizeof(linie), 0, (struct sockaddr *) &client, sizeof(client));
        sendto(s,&coloana, sizeof(coloana), 0, (struct sockaddr *) &client, sizeof(client));
        }


        close(s);
}
