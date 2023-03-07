#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <time.h>
#include <fcntl.h>

int main(int argc, char** argv) {
	
	mkfifo("./fifoAB", 0600);
        mkfifo("./fifoBA", 0600);


	int fd_write = open("fifoAB",O_WRONLY);
	int fd_read = open("fifoBA", O_RDONLY);

	srandom(getpid());
	int nr = random() % 10001 + 1000;
	printf("A a generat %d\n", nr);
	int x = -1;
	char ch;
	while(nr != x) {
		read(fd_read, &x, sizeof(int));
		if(nr<x)
			ch = '<';
		if(nr>x)
			ch='>';
		if(nr == x)
			ch='=';
		printf("B trimite lui A %d, iar A trimite lui B %c\n", x, ch);
		write(fd_write, &ch, sizeof(char));
	}

	close(fd_write);
	close(fd_read);
	unlink("fifoAB");
	unlink("fifoBA");
	return 0;



}	
