#include <stdlib.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>

int main() {
  int s;
  struct sockaddr_in server, client;
  int c, l, i,d;
  int ok=1;
  uint16_t k, old = 0;

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

  recvfrom(s, &k, sizeof(k), MSG_WAITALL, (struct sockaddr *) &client,(socklen_t *) &l);
  k = ntohs(k);
  printf("Am primit: %hu\n", k);
  if(k<2)
        ok=1;
  if(k==2)
        ok=1;
  if(k!=2 && k%2==0)
        ok=0;
  for(d=2;d<=k/2;d++){
        if(k%d==0)
                ok=0;
  }
  ok=htons(ok);
  sendto(s,&ok,sizeof(ok),0,(struct sockaddr*) &client,sizeof(client));
  close(s);
}
