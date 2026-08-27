/**
* -------------------------------------
* @file Q1_file.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-07-26)
*
* -------------------------------------
*/

#include <pthread.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

//global variables
#define MAX_RESOURCES 5
int available_resources = MAX_RESOURCES;
#define NUM_THREADS 5
pthread_mutex_t lock;

/* decrease available_resources by count resources */
/* return @ if sufficient resources available, */
/* otherwise return -1 */
int decrease_count(int thread_number, int count) {
    pthread_mutex_lock(&lock);
    if (available_resources < count){
        pthread_mutex_unlock(&lock);
        return -1;
    }
    else {
        available_resources -= count;
        printf("The thread %d has acquired %d resources and %d more resources are available.\n", thread_number, count, available_resources) ;
        pthread_mutex_unlock(&lock);
        return 0;
    }
}

/* increase available resources by count */
int increase_count(int thread_number, int count) {
    pthread_mutex_lock(&lock);
    available_resources += count;
    printf("The thread %d has released %d resources and %d resources are now available.\n", thread_number, count, available_resources);
    pthread_mutex_unlock(&lock);
    return 0;
}

void *thread_function (void* arg){
    int thread_number = *(int*)arg;
    int resource_acquired = decrease_count (thread_number, 1);
    
    //if resource not acquired print error
    if (resource_acquired == -1){
        printf("Threads %d could not acquire enough resources\n",thread_number);
    }
    //else sleep for 1 second then return resource
    else{
        sleep(1);
        increase_count(thread_number, 1);
    }

    //free memory allocated for thread number
    free(arg);

    pthread_exit (NULL);
}

//main function
int main(){
    //define threads
    pthread_t threads [NUM_THREADS];

    //create threads
    for (int x = 0;x<NUM_THREADS;x++){
        int* thread_num = malloc(sizeof(int));
        *thread_num = x;
        pthread_create(&threads[x], NULL, thread_function, thread_num);
    }

    //join threads
    for (int x = 0; x<NUM_THREADS;x++){
        pthread_join(threads[x],NULL);
    }

    printf("All threads have finished execution. Available resources: %d\n", available_resources);
    return 0;

}