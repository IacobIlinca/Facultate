#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>
#include <stdlib.h>

int main() {
	int s;
	struct sockaddr_in server, client;
	int c, l, i;
	uint16_t k, old = 0;

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
  
     recvfrom(s, &k, sizeof(k), MSG_WAITALL, (struct sockaddr *) &client,(socklen_t *) &l);
    k = ntohs(k);
//    printf("Am primit: %hu la pasul %d\n", k, i+1);
    printf("Am primit pe %hu ", k);
    
    int ok = 1;
    for(i=2;i<k/2;i++) {
		if(k%i == 0) ok=0;
    }

   sendto(s, &ok, sizeof(ok), 0, (struct sockaddr *) &client, &l);

  
  
  close(s);
}
