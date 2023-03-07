#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>

int n;
int list[10];

void* routine(void* arg) {
	int k;
	k = *(int*)arg;
	free(arg);
	printf("Thread ul  cu nr %d\n", k);
	return NULL;
}


int main(int argc, char** argv) {
	int i;
	printf("n= ");
	scanf("%d",&n);
	pthread_t th[n];
	for(i=0;i<n;i++) {
		int* k = malloc(sizeof(int));
		*k = i;
		if(pthread_create(&th[i], NULL, routine, k)) {
			perror("Failed to create thread");
		}
	}
	for(i=0;i<n;i++) {
		if(pthread_join(th[i], NULL)) {
			perror("Failed to join thread");
		}
	}
	return 0;
}
