/**
* -------------------------------------
* @file Q2_file.c
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
#include <sys/mman.h>
#include <sys/stat.h>        
#include <fcntl.h>

#define SHM_SIZE 1024

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
    //if parameters given aren't 2, output the correct way to input
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <positive integer>\n", argv[0]);
        return 1;
    }

    //make n the number input by user
    int n = atoi(argv[1]);

    //if n is less than 0, print error message (error checking)
    if (n <= 0) {
        fprintf(stderr, "Please provide a positive integer greater than 0.\n");
        return 1;
    }

    int shm_fd;
    void *shm_ptr;

    //open shared memory
    shm_fd = shm_open("/collatz_shm", O_CREAT | O_RDWR, 0666);

    //if open failed, print error
    if (shm_fd == -1){
        perror("shm_open failed");
        exit(1);
    }

    //set size of shared memory
    if (ftruncate(shm_fd, SHM_SIZE) == -1){
        perror("ftruncate failed");
        exit (1);
    }

    //map shared memory into the process's address space
    shm_ptr = mmap(NULL, SHM_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
    //if mapping failed, print error
    if (shm_ptr == MAP_FAILED){
        perror("mmap failed");
        exit(1);
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
        //write beginning number to shared memory
        int written = sprintf((char *)shm_ptr, "%d",n);
        
        //while n does not =1, invoke the function to get next number in sequence
        do {
            n = collatz_conjecture(n);  

            //write result of function to shared memory
            written += sprintf((char *)shm_ptr + written, ", %d",n);

        }while (n != 1);
        exit(0);
    }

    //parent process
    else{
        printf("Parent Process created\n");

        //wait for child to finish
        wait(NULL);

        //print final results from shared memory
        printf("Output from shared memory: %s\n", (char *)shm_ptr);

        //unmap the shared memory
        if (munmap(shm_ptr, SHM_SIZE) == -1) {
            perror("munmap failed");
        }

        //remove the shared memory object
        if (shm_unlink("/collatz_shm") == -1) {
            perror("shm_unlink failed");
        }
    }

    return 0;
}