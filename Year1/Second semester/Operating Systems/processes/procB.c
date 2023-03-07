#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <time.h>
#include <fcntl.h>

int main(int argc, char** argv)  {


	int fd_write = open("fifoAB",O_WRONLY);
	int fd_read = open("fifoBA", O_RDONLY);
	char ch = 'x';
	int mn = 1000;
	int mx = 10000;
	srandom(getpid());
	while(ch != '=') {
		int r = (random() % (mx-mn+1)) + mn;
		write(fd_write, &r, sizeof(int));
		read(fd_read, &ch, sizeof(char));
		if(ch == '<') 
			mx = r;
		if(ch == '>')
			mn = r;
		}
	close(fd_write);
	close(fd_read);
return 0;
}
