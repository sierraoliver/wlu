/**
* -------------------------------------
* @file Q3_file.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-06-13)
*
* -------------------------------------
*/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

//global varaibles
int average, count, minimum, maximum;
int *numbers;

//function to calculate the average 
void *calculate_average (void *arg){
    int sum = 0;

    //add up all numbers input
    for (int x = 0; x<count;x++){
        sum += numbers[x];
    }

    //divide total sum by amount of #'s
    average = sum/count;
    pthread_exit(0);

}

//function to calculate the minimum
void *calculate_minimum (void *arg){
    minimum = numbers[0];

    //search numbers for lowest value
    for (int x = 0; x<count;x++){
        if (numbers[x]<minimum){
            minimum = numbers[x];
        }
    }
    pthread_exit(0);
}

//function to calculate the maximum
void *calculate_maximum (void *arg){
    maximum = numbers[0];

    //search numbers for highest value
    for (int x = 0; x<count;x++){
        if (numbers[x]>maximum){
            maximum = numbers[x];
        }
    }
    pthread_exit(0);
}

int main (int argc, char *argv[]){
    //validate that at least one number is provided
    if (argc <2){
        printf("Usage: num1, num2, num3, ....\n");
        printf("Enter multiple numbers to calculate avg, min and max\n");
        return 1;
    }

    count = argc-1; //make count the amount of numbers input

    //allocate memory for input numbers
    numbers = (int*)malloc(count*sizeof(int)); 
    if (numbers == NULL){
        perror("Memory allocation failed");
        return 1;
    }

    //convert input arguments to integers
    for (int x = 0; x<count;x++){
        numbers[x] = atoi(argv[x+1]);
    }

    pthread_t avg_thread, min_thread, max_thread;

    //create each thread and if fails, print error
    if (pthread_create (&avg_thread, NULL, calculate_average, NULL)!=0){
        perror ("Failed to create average thread");
        return 1;
    }
    if (pthread_create (&max_thread, NULL, calculate_maximum, NULL)!= 0){
        perror ("Failed to create max thread");
        return 1;
    }
    if (pthread_create (&min_thread, NULL, calculate_minimum, NULL)!= 0){
        perror ("Failed to create min thread");
        return 1;
    }
    

    //wait for all threads to complete
    if (pthread_join(avg_thread, NULL)!= 0){
        perror("Failed to join average thread");
        return 1;
    }
    if (pthread_join(max_thread, NULL)!= 0){
        perror("Failed to join max thread");
        return 1;
    }
    if (pthread_join(min_thread, NULL)!= 0){
        perror("Failed to join min thread");
        return 1;
    }


    //print the results of the different threads
    printf("The average value is %d\n", average);
    printf("The minimum value is %d\n", minimum);
    printf("The maximum value is %d\n", maximum);

    //free allocated memory
    free (numbers);

    return 0;
}