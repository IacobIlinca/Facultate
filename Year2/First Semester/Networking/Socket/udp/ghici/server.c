#include <stdlib.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <time.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>

int main() {
  int s;
  struct sockaddr_in server, client;
  int c, l,i;
  char buffer[101];
  uint16_t k=0;
  srand(time(0));

  s = socket(AF_INET, SOCK_DGRAM, 0);
  if (s < 0) {
    printf("Eroare la crearea socketului server\n");
    return 1;
  }

  memset(&server, 0, sizeof(server));
  server.sin_port = htons(2105);
  server.sin_family = AF_INET;
  server.sin_addr.s_addr = INADDR_ANY;

  if (bind(s, (struct sockaddr *) &server, sizeof(server)) < 0) {
    printf("Eroare la bind\n");
    return 1;
  }

  l = sizeof(client);
  memset(&client, 0, sizeof(client));
	int pauza = 1;

	int g;
	g = rand()%100;
	printf("S-a generat: ");
	printf("%d", g);
	printf("\n");
	//sendto(s, &g, 0, (struct sockaddr*) &client, sizeof(client));
	while(pauza == 1){
	int nr;
	recvfrom(s, &nr, sizeof(nr), 0, (struct sockaddr*) &client,(socklen_t *) &l);
	nr = ntohs(nr);
	int ok;
	if( nr > g) {
		ok = 1;
		ok = htons(ok);
		sendto(s, &ok, sizeof(ok), 0, (struct sockaddr*) &client, sizeof(client));
	}
	if( nr < g) {
		ok = 2;
		ok = htons(ok);
		sendto(s, &ok, sizeof(ok), 0, (struct sockaddr*) &client, sizeof(client));
	}
	else {
		ok = 0;
		ok = htons(ok);
		sendto(s, &ok, sizeof(ok), 0, (struct sockaddr*) &client, sizeof(client));
		pauza = 0;

	}
	}
close(s);
}

