/**
* -------------------------------------
* @file Q1_file.c
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
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

//method to determine next number in collatz sequence
int collatz_conjecture(int n){
    //if n is an even number
    if (n%2 == 0){
        n/= 2;
    }

    //if n is an odd number
    else{
        n = n * 3 +1;
    }

    return n;
}


int main(int argc, char *argv[]){
    //if parameters given are less than 2, output the correct way to input
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <positive integer>\n", argv[0]);
        return 1;
    }

    //make n the number input by user
    int n = atoi(argv[1]);

    //if n is less than 0, print error message
    if (n <= 0) {
        fprintf(stderr, "Please provide a positive integer greater than 0.\n");
        return 1;
    }

    //fork to create a child process
    pid_t pid;
    pid = fork();

    if (pid<0){
        perror("fork failed");
        exit(1);
    }

    //child process
    else if (pid == 0){
        printf("Child Process created: Collatz sequence starting at %d\n", n);

        //print out beginning of sequence
        printf("%d",n);

        //invoke function while n is not 1
        do {
            n = collatz_conjecture(n);  

            //print result from function
            printf(", %d", n);

        }while (n != 1);
        printf("\n");
        exit(0);
    }

    //parent process
    else{
        printf("Parent Process created\n");
        wait(NULL);
    }

    return 0;
}