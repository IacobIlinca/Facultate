#include <unistd.h>
#include <time.h>
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
	srand(time(0));

        c = socket(AF_INET, SOCK_DGRAM, 0);
        if (c < 0) {
                printf("Eroare la crearea socketului client\n");
                return 1;
        }

        memset(&server, 0, sizeof(server));
        server.sin_port = htons(2105);
        server.sin_family = AF_INET;
        server.sin_addr.s_addr = inet_addr("127.0.0.1");

	while(1) {
		int nr;
		nr = rand() %100;
		printf("S-a ghicit: ");
		printf("%d", nr);
		printf("\n");
		nr = htons(nr);
		sendto(c, &nr, sizeof(nr), 0, (struct sockaddr *) &server, sizeof(server));

		int ok;
		recvfrom(c,&ok,sizeof(ok), MSG_WAITALL, (struct sockaddr*) &server,(socklen_t *)&l);
		ok = ntohs(ok);
		
		printf("Am primit: ");
		printf("%d\n", ok);

		if(ok==0) break;
	}
	close(c);
}

