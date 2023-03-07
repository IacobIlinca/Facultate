#include <stdio.h>
#include <pthread.h>
#define MAX_THR 100

void* f(void* a)
{
	int k = *(int*) a;
	printf("eu sunt thread-ul %d\n", k);
	return NULL;
}

int main(int argc, char** argv) 
{
	pthread_t tid[MAX_THR];
	int i;
	for(i=0;i<MAX_THR;i++)
	{
		pthread_create(&tid[i], NULL, f, &i);
	}
	for(i=0;i<MAX_THR;i++)
	{
		pthread_join(tid[i], NULL);
	}
	return 0;
}
	   
