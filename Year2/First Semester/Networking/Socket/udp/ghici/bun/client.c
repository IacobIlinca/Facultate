#include <sys/types.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
int main() {
        int c,l;
        struct sockaddr_in server;
        uint16_t a, b, suma, i, k;
        uint16_t prim;

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

	int rez = 0;
	int old = rand()%100 + 1;
	int nr = 0;
	printf("%d\n", old);
	old = htons(old);
	sendto(c, &old, sizeof(old), 0,(struct sockaddr *) &server, sizeof(server));

	recvfrom(c,&rez, sizeof(rez),0,(struct sockaddr *) &server, (socklen_t*) &l);
	rez = ntohs(rez);
	old = ntohs(old);

	while(rez != 1) {
		if(rez == 0) nr = rand()%old + 1;
		if(rez == 2) nr = rand()%(100-old) + 1;

		printf("%d\n", nr);
		old = nr;
		nr = htons(nr);
		sendto(c, &nr, sizeof(nr), 0,(struct sockaddr*)&server, sizeof(server));
		recvfrom(c, &rez, sizeof(rez), 0, (struct sockaddr*) &server, (socklen_t*) &l);
		rez = ntohs(rez);
	}
	close(c);
}
