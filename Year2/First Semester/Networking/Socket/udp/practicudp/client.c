#include<stdio.h>
#include <unistd.h>
#include<string.h>
#include<stdlib.h>
#include<arpa/inet.h>
#include<sys/socket.h>

#define SERVER "127.0.0.1"
#define BUFLEN 512
#define PORT 1234

int main(int argc, char** argv)
{
    struct sockaddr_in serveraddr;
	struct sockaddr_in serveraddr1,clientaddr;
    int s, i, slen=sizeof(serveraddr),s1, clientaddr,nr1,rez;
        char nr[512],buf[512],bufr[512];

    s=socket(AF_INET, SOCK_DGRAM, 0);
s1=socket(AF_INET, SOCK_DGRAM, 0);

    memset((char *) &serveraddr, 0, sizeof(serveraddr));
    serveraddr.sin_family = AF_INET;
    serveraddr.sin_port = htons(atoi(argv[2]));
    serveraddr.sin_addr.s_addr = inet_addr(argv[1]);

    printf("Sirul=");
    gets(buf);
    sendto(s, &buf, strlen(buf)*sizeof(char) , 0 , (struct sockaddr *) &serveraddr, slen);

	printf("\nNumarul= ");
	scanf("%s",&nr);
        sendto(s, &nr, strlen(nr)*sizeof(char), 0, (struct sockaddr *) &serveraddr,slen);
	
 memset((char *) &serveraddr1, 0, sizeof(serveraddr1));
    serveraddr1.sin_family = AF_INET;
    serveraddr1.sin_port = htons(nr);
    serveraddr1.sin_addr.s_addr = inet_addr(argv[1]);

	recvfrom(s1, &bufr, sizeof(bufr), 0, (struct sockaddr1 *) &clientaddr, &slen);
	printf("%s", bufr);


		
   close(s);
}
