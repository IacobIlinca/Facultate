#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>
int n,max_thr;
int list[30000];
int suma[30];
int dif[30];
int dif_min = 1000000000;
pthread_barrier_t bar;
pthread_mutex_t mut;

void* citire(void* arg) {
	int i;
	for(i=0;i<n;i++) {
		list[i] = rand() % 100;
	}
	//printf("aici nu");
	return NULL;
}

void* routine(void* arg) {
	int k = *(int*) arg;
	free(arg);
	int m = rand() % 256;
	int i;
	for(i=k*3000;i<k*3000+3000;i++) {	
		suma[k] += list[i];	
	}
	suma[k] = suma[k] / 3000;
	pthread_barrier_wait(&bar);
	for(i=0;i<max_thr;i++) {
		
		dif[i] = abs(dif[i] - m);
		pthread_mutex_lock(&mut);
		if(dif[i]<dif_min) {
	        	dif_min = dif[i];
		}
		pthread_mutex_unlock(&mut);
       				       
	}
	for(i=0;i<max_thr;i++) {
		printf("dif minima:%d\n", dif[i]);
	}

	return NULL;
}

int main() {
	scanf("%d",&n);
	max_thr = n/3000;
	pthread_t th[max_thr], tc;
	pthread_barrier_init(&bar, NULL, max_thr);
	pthread_mutex_init(&mut, NULL);
	int i;
	srand(time(NULL));
	pthread_create(&tc, NULL, citire, NULL); 
	pthread_join(tc, NULL);
	for(i=0;i<max_thr;i++) {
		int* ar = malloc(sizeof(int));
		*ar = i;
		pthread_create(&th[i],NULL, routine, ar);
	}
	for(i=0;i<max_thr;i++) {
		pthread_join(th[i], NULL);
	}
	printf("dif min:%d", dif_min);
	pthread_barrier_destroy(&bar);
	pthread_mutex_destroy(&mut);
	return 0;
}
