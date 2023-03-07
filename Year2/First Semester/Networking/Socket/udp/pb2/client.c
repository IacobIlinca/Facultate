#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <unistd.h>

int main() {
	int c;
	struct sockaddr_in server;
	uint16_t a, b, suma, i, k;
	int l;

	c = socket(AF_INET, SOCK_DGRAM, 0);
	if (c < 0) {
		printf("Eroare la crearea socketului client\n");
		return 1;
	}

	memset(&server, 0, sizeof(server));
	server.sin_port = htons(2811);
	server.sin_family = AF_INET;
	server.sin_addr.s_addr = inet_addr("127.0.0.1");

	printf("dati un nr: ");  
	scanf("%hu", &k);
	printf("%hu", k);
	k = htons(k);
	int ok;
	sendto(c, &k, sizeof(k), 0, (struct sockaddr *) &server, sizeof(server));
	recvfrom(c,&ok,sizeof(ok), MSG_WAITALL, (struct sockaddr*) &server,(socklen_t *)&l);
  
	ok = ntohs(ok);
   if(ok == 0)  {
	printf("Numarul NU e prim!");
   } else {
	printf("Numarul e prim!");
   }
  
  close(c);
}
