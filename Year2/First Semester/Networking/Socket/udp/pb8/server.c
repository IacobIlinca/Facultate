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

 int nr1, nr2;
 recvfrom(s,&nr1, sizeof(nr1),0,(struct sockaddr*)&client, (socklen_t*)&l);
 recvfrom(s,&nr2, sizeof(nr2),0,(struct sockaddr*)&client, (socklen_t*)&l);
nr1 = ntohs(nr1);
nr2 = ntohs(nr2); 
printf("NR1= %d", nr1);
 printf("\nNR2= %d",nr2);

 int cmmmc = nr1, ok=0,cmmdc=1;
 while(ok==0) {
	if(cmmmc%nr1==0 && cmmmc%nr2 ==0) {
		ok = 1;}
	else cmmmc++;
	}
 printf("cmmmc = %d", cmmmc);

 int d = 1;
 while(nr1%d!=0 && nr2%d!= 0) d++;
cmmdc = d;
 printf("cmmdc = %d", cmmdc);
	
cmmdc = htons(cmmdc);
cmmmc = htons(cmmmc);
	sendto(s, &cmmmc, sizeof(cmmmc),0,(struct sockaddr*)&client, sizeof(client));
	sendto(s, &cmmdc, sizeof(cmmdc),0,(struct sockaddr*)&client, sizeof(client));
close(s);
}
