/**
* -------------------------------------
* @file Q2_file.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-06-23)}
*
* -------------------------------------
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_THREADS 100

typedef struct {
    int pid;
    int arr_time;
    int burst_time;
    int waiting_time;
    int turn_around_time;
} Thread;

int main(int argc, char *argv[]){
    if (argc == 0){
        fprintf(stderr, "Enter a file to check FCFS scheduling\n");
        return 1;
    }

    Thread threads[MAX_THREADS];
    int n = 0;
    char *file_name;
    FILE *ptr;

    file_name = argv[0];

    ptr = fopen(file_name, "r");
    if (ptr == NULL){
        perror("File open failed");
        return 1;
    }

    //read the file data into the threads array
    while (fscanf(fp, "%s %d %d", threads[n].tid, &threads[n].arrival_time, &threads[n].burst_time) == 3) {
        n++;
    }
    fclose(ptr);

    // Sort by arrival time
    for (int x=0; x<n-1; x++) {
        for (int y=0;y<n-x-1; y++) {
            if (threads[y].arrival_time > threads[y + 1].arrival_time) {
                Thread temp = threads[y];
                threads[y] = threads[y + 1];
                threads[y + 1] = temp;
            }
        }
    }

    int current_time = 0;
    float total_waiting = 0, total_turnaround = 0;

    for (int x = 0;x< n;x++) {
        if (current_time < threads[x].arrival_time)
            current_time = threads[x].arrival_time;

        threads[x].waiting_time = current_time - threads[x].arrival_time;
        threads[x].completion_time = current_time + threads[x].burst_time;
        threads[x].turn_around_time = threads[x].completion_time - threads[x].arrival_time;

        current_time = threads[x].completion_time;

        total_waiting += threads[x].waiting_time;
        total_turnaround += threads[x].turn_around_time;
    }

    //print results
    printf("\nAverage Waiting Time: %.2f\n", total_waiting / n);
    printf("Average Turnaround Time: %.2f\n", total_turnaround / n);

    return 0;

}