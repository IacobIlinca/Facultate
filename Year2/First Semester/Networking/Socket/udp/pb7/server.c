#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>

int main() {

        int s;
        struct sockaddr_in server,client;

        int l;

        s=socket(AF_INET,SOCK_DGRAM,0);
        if(s<0){
                printf("Eroare la crearea socketului server \n");
                return 1;
        }
        memset(&server,0,sizeof(server));
        server.sin_port=8554;
        server.sin_family=AF_INET;
        server.sin_addr.s_addr=INADDR_ANY;
        if(bind(s,(struct sockaddr *) &server,sizeof(server))<0){
                printf("Eroare la bind \n");
                return 1;
        }

        l=sizeof(client);
        memset(&client,0,sizeof(client));
                int i=1,p=0,n=0,j=0;
                char sir[120],subsir[120]={};

                recvfrom(s,sir,120,MSG_WAITALL, (struct sockaddr *) &client,(socklen_t) &l);
                recvfrom(s,&i,sizeof(i),MSG_WAITALL,(struct sockaddr *) &client, (socklen_t) &l);
                recvfrom(s,&p,sizeof(p),MSG_WAITALL,(struct sockaddr *) &client,(socklen_t) &l);
                printf("%s\n%d\n%d\n", sir, ntohs(i), ntohs(p));
                i = ntohs(i);
                p = ntohs(p);
                while(n<strlen(sir) && p>0){
                        if(n>=i){
                                subsir[j]=sir[n];
                                j++;
                                p--;
                        }
                        n++;
                }

        sendto(s,subsir,strlen(subsir),0,(struct sockaddr *) &client, l);
        close(s);
        }
