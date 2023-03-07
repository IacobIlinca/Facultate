#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<arpa/inet.h>
#include <unistd.h>
#include<sys/socket.h>

#define BUFLEN 512
#define PORT 1234

int main(int argc, char** argv)
{
    struct sockaddr_in serveraddr, clientaddr;
	struct sockaddr_in serveraddr1,clientaddr1;
    int s,s1, i, slen = sizeof(clientaddr) , nr,nr2, rez=0;
        char nr1[512],buf1[512],buf2[512], bufr[512];

    s=socket(AF_INET, SOCK_DGRAM, 0);
s1=socket(AF_INET, SOCK_DGRAM, 0);

    memset((char *) &serveraddr, 0, sizeof(serveraddr));
    serveraddr.sin_family = AF_INET;
    serveraddr.sin_port = htons(atoi(argv[2]));
    serveraddr.sin_addr.s_addr = inet_addr(argv[1]);

    bind(s , (struct sockaddr*)&serveraddr, sizeof(serveraddr));

    printf("Waiting for data...\n");
    memset((char *) &buf1, 0, sizeof(buf1));
    recvfrom(s, &buf1, sizeof(buf1), 0, (struct sockaddr *) &clientaddr, &slen);

   printf("S-a primit numele: ");
   printf("%s",buf1);

   memset((char *)&nr1, 0, sizeof(nr1));
   recvfrom(s, &nr1,sizeof(nr1), 0, (struct sockaddr*) &clientaddr, &slen);
   nr = atoi(nr1);
   printf("\nS-a primit numarul: ");
   printf("%d", nr);

   char alf[512]="abcdefghijklmnopqrstuvwxyz";
   
   for(i=0;i<strlen(buf1);i++) {
	int ok=0,j=0;
        while(ok ==0 ){
	if(buf1[i]!=' '){
		if(buf1[i] == alf[j]) {
			ok = 1;
			buf1[i] = alf[26-i+1];
			//printf("%s", buf1[i]);
		}}
	j ++;
	}
   }
   /*
    for(i=0;i<strlen(buf1);i++){
       if(buf1[i] == 'a') buf1[i] ='z';
       if(buf1[i] == 'b') buf1[i] ='y';
	if(buf1[i] == 'c') buf1[i] ='x';
	if(buf1[i] == 'd') buf1[i] ='w';
}*/	

	memset((char *) &serveraddr1, 0, sizeof(serveraddr1));
    serveraddr1.sin_family = AF_INET;
    serveraddr1.sin_port = htons(nr);
    serveraddr1.sin_addr.s_addr = inet_addr(argv[1]);

    bind(s1 , (struct sockaddr*)&serveraddr1, sizeof(serveraddr1));
	

  //printf("%s",buf1);
  sendto(s1,&buf1, strlen(buf1)*sizeof(char), 0, (struct sockaddr1*)&clientaddr, slen);
   
  close(s);
}
