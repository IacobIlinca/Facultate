#include <stdio.h>
#include <unistd.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>

int main() {
  int s;
  struct sockaddr_in server, client;
  int c, l,i;
  char buffer[101],x;
  uint16_t k=0,sol[101];

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

  recvfrom(s, buffer, sizeof(buffer), MSG_WAITALL, (struct sockaddr *) &client,(socklen_t *) &l);
  printf("Am primit: %s\n", buffer);
  recvfrom(s,&x,sizeof(x),MSG_WAITALL,(struct sockaddr *)&client,(socklen_t *)&l);
  for(i=0;i<strlen(buffer);i++)
  {
        if(buffer[i]==x)
        {
                sol[k]=i;
                k++;
        }
  }
  k=htons(k);
  sendto(s,&k,sizeof(k),0,(struct sockaddr*) &client,sizeof(client));
  k=ntohs(k);
  for(i=0;i<k;i++)
  {
        sol[i]=htons(sol[i]);
        sendto(s,&sol[i],sizeof(sol[i]),0,(struct sockaddr*) &client,sizeof(client));
  }
  close(s);
}
