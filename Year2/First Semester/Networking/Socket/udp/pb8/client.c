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

	printf("Primul numar este: ");
	int nr1, nr2;
	scanf("%d", &nr1);
	printf("\nAl doilea numar este: ");
	scanf("%d", &nr2);

	nr1 = htons(nr1);
	nr2 = htons(nr2);

	sendto(c, &nr1, sizeof(nr1), 0,(struct sockaddr*)&server, sizeof(server));
	sendto(c, &nr2, sizeof(nr2), 0,(struct sockaddr*)&server, sizeof(server));

	int cmmdc, cmmmc;
	recvfrom(c,&cmmdc, sizeof(cmmdc), 0,(struct sockaddr *)&server,(socklen_t*)&l);
	recvfrom(c,&cmmmc, sizeof(cmmmc), 0,(struct sockaddr *)&server,(socklen_t*)&l);

	cmmmc = ntohs(cmmmc);
	cmmdc = ntohs(cmmdc);
	int aux;
	if(cmmmc <cmmdc) {
		printf("S-a primit aiurea!");
		aux = cmmmc;
		cmmmc = cmmdc;
		cmmdc = aux;
	}

	printf("\nCmmdc este: %d", cmmdc);
	printf("\nCmmmc este: %d", cmmmc);
	close(c);
}
	
