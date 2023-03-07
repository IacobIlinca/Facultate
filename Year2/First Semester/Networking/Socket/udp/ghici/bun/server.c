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
        int s;
        struct sockaddr_in server, client;
        int c, l, i;
        uint16_t k;
        uint16_t prim = 1;
        char buffer[101];
        uint16_t cnt=0;
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
	int nr = rand() %100 + 1;
	printf("NR = %d\n", nr);

	int ghicit= 0;
	int nr_client = 0;
	int rez = 0;
	
	while(rez != 1) {
		recvfrom(s, &nr_client, sizeof(nr_client), 0,(struct sockaddr *)&client, (socklen_t*) &l);
		nr_client = ntohs(nr_client);
		printf("Am primit de la client: %d\n", nr_client);

		if(nr < nr_client) rez = 0;
		else if (nr > nr_client) rez = 2;
		else rez = 1;

		rez = htons(rez);
		sendto(s, &rez, sizeof(rez), 0, (struct sockaddr*) &client, sizeof(client));
	}
	close(s);
}

