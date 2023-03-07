#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <sys/wait.h>

int main(int argc, char** argv) {
	FILE* file = fopen("rez.txt", "w");

	if(file==NULL) {
		perror("nu se deschide");
		exit(1);
	}

	int n;
	printf("n= ");
	scanf("%d", &n);

	int p2a[2], a2b[2], b2c[2], c2a[2];

	int ok1=pipe(p2a);
	if(ok1==-1) {
		perror("pipe()");
		exit(1);
	}
	int ok2=pipe(a2b);
	if(ok2==-1) {
		perror("pipe()");
		exit(1);
	}
	int ok3=pipe(b2c); 
	if(ok3==-1) {
		perror("pipe()");
		exit(1);
	}

	int ok4=pipe(c2a);
	if(ok4==-1) {
		perror("pipe()");
		exit(1);
	}

	int pid=fork();
	if(pid==-1){
		perror("fork()");
		exit(1);
	}
	int pid2=fork();
	if(pid2==-1) {
		perror("fork()");
		exit(1);
	}
	int pid3=fork();
	if(pid3==-1) {
		perror("fork()");
		exit(1);
	}

	if(pid==0) {
		//A
		close(p2a[1]);
		close(a2b[0]); close(b2c[1]);
		close(b2c[0]); close(c2a[1]);
		close(c2a[0]);
		int caz = 1;

		while(1) {
			if(caz == 1)  {
				int n;
				read(p2a[0],&n,sizeof(int));
				if(n%6 == 0  || n%10==6) {
					fprintf(file, "boltz");

				} 
				n++;
				write(a2b[1],&n,sizeof(int));
			} else {
				read(p2a[0],&n,sizeof(int));
				if(n%6 == 0  || n%10==6) {
					fprintf(file, "boltz");
				}								                                n++;
				write(a2b[1],&n,sizeof(int));
			}	

		}
	}


}
