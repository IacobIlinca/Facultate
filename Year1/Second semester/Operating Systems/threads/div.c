#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int k,n,max_th, diviz = 0;
int list[30000000];
pthread_barrier_t bar;
pthread_mutex_t mut;

void* reads(void* arg) {
	int i;
	int fd = open("rnd_file", O_RDONLY);
	for(i=0;i<n;i++) {
		read(fd, &list[i], 1);
	}
	printf("Citire finalizata cu succes\n");
	return NULL;
}

void* routine(void* arg) {
	int ar = *(int*) arg;
	free(arg);
	int nr = 0,i;
	for(i=ar*2000;i<ar*2000+2000;i++) {
		if(list[i]%k == 0) {
			nr++;
		}
	}
	pthread_barrier_wait(&bar);

	pthread_mutex_lock(&mut);
	diviz += nr;
	pthread_mutex_unlock(&mut);
	return NULL;
}



int main(int argc, char** argv) {
	int i;
	printf("k = ");
	scanf("%d", &k);
	printf("n = ");
	scanf("%d", &n);
	max_th = n/2000;
	pthread_barrier_init(&bar, NULL, max_th);
	pthread_mutex_init(&mut, NULL);
	pthread_t th[max_th], tc;
	pthread_create(&tc, NULL, reads, NULL);
	pthread_join(tc,NULL);
	for(i=0;i<max_th;i++) {
		int* ar = malloc(sizeof(int));
		*ar = i;
		if(pthread_create(&th[i], NULL, routine, ar)) {
			perror("Failed to create thread");
		}
	}

	for(i=0;i<max_th;i++) {
		if(pthread_join(th[i], NULL)) {
			perror("Failed to join thread");
		}
	}
	pthread_barrier_destroy(&bar);
	pthread_mutex_destroy(&mut);
	printf("nr divizibile cu k: %d\n", diviz);
	
	return 0;
}
