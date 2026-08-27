/**
* -------------------------------------
* @file Q1_file.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-08-06)
*
* -------------------------------------
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//global variables
#define NUMBER_OF_CUSTOMERS 5
#define NUMBER_OF_RESOURCES 4
/* the available amount of each resource */
int available [NUMBER_OF_RESOURCES];
/*the maximum demand of each customer */
int maximum [NUMBER_OF_CUSTOMERS] [NUMBER_OF_RESOURCES];
/* the amount currently allocated to each customer */
int allocation [NUMBER_OF_CUSTOMERS] [NUMBER_OF_RESOURCES];
/* the remaining need of each customer */
int need [NUMBER_OF_CUSTOMERS] [NUMBER_OF_RESOURCES];

int is_safe_state(){
    //initialize work and finish
    int work [NUMBER_OF_RESOURCES];
    int finish [NUMBER_OF_CUSTOMERS] = {0};

    for (int x = 0; x<NUMBER_OF_RESOURCES;x++){
        work[x] = available[x];
    }

    //repeat until no more customers can finish safely
    while (1){
        int found = 0;

        //try to find an unfinished customer who needs can be met with current work
        for (int x = 0; x< NUMBER_OF_CUSTOMERS; x++){
            if (!finish[x]){

                int can_finish = 1;
                //check if customer's need <= work for all resources
                for (int y = 0; y<NUMBER_OF_RESOURCES; y++){
                    if (need[x][y] > work[y]){
                        can_finish = 0;
                        break;
                    }
                }

                if (can_finish){
                    //simulate customer finishing
                    for (int y = 0; y<NUMBER_OF_RESOURCES; y++){
                        work[y] += allocation[x][y];
                    }

                    finish[x] = 1;
                    found = 1;
                }
            }
        }
        if (!found){
            //no customers can finish
            break;
        }
    }

    //if all customers can finish, system is safe
    for (int x = 0; x<NUMBER_OF_CUSTOMERS;x++){
        if (!finish[x]){
            return 0;
        }
    }

    return 1;
}

int request_resources (int customer_num, int request[]){
    //check if request exceeds need or available resources
    for (int i = 0; i < NUMBER_OF_RESOURCES; i++) {
        if (request[i] > need[customer_num][i]) return -1;
        if (request[i] > available[i]) return -1;
    }

    //allocate resources temporarily
    for (int i = 0; i < NUMBER_OF_RESOURCES; i++) {
        available[i] -= request[i];
        allocation[customer_num][i] += request[i];
        need[customer_num][i] -= request[i];
    }

    //check if safe state
    if (!is_safe_state()) {

        //take back request if not in safe state
        for (int i = 0; i < NUMBER_OF_RESOURCES; i++) {
            available[i] += request[i];
            allocation[customer_num][i] -= request[i];
            need[customer_num][i] += request[i];
        }

        return -1;
    }

    return 0;
}

void release_resources (int customer_num, int release[]){
    for (int i = 0; i < NUMBER_OF_RESOURCES; i++) {
        //ensure release amount does not exceed allocation
        if (release[i] > allocation[customer_num][i]) {
            release[i] = allocation[customer_num][i]; 
        }

        available[i] += release[i];
        allocation[customer_num][i] -= release[i];
        need[customer_num][i] += release[i];
    }
}

//print all data structures
void print_state(){
    printf("\nAvailable:\n");
    for (int x = 0; x<NUMBER_OF_RESOURCES;x++){
        printf("%d ",available[x]);
    }

    printf("\nMaximum:\n");
    for (int x = 0; x<NUMBER_OF_CUSTOMERS;x++){
        for( int y = 0; y<NUMBER_OF_RESOURCES;y++){
            printf("%d ", maximum[x][y]);
        }
        printf("\n");
    }

    printf("\nAllocation:\n");
    for (int x = 0; x<NUMBER_OF_CUSTOMERS;x++){
        for( int y = 0; y<NUMBER_OF_RESOURCES;y++){
            printf("%d ", allocation[x][y]);
        }
        printf("\n");
    }

    printf("\nNeed:\n");
    for (int x = 0; x<NUMBER_OF_CUSTOMERS;x++){
        for( int y = 0; y<NUMBER_OF_RESOURCES;y++){
            printf("%d ", need[x][y]);
        }
        printf("\n");
    }

    return;
}

int main (int argc, char *argv[]){
    if (argc != NUMBER_OF_RESOURCES + 1){
        printf("Usage: %s <R1> <R2> <R3> <R4>\n",argv[0]);
        return 1;
    }

    //initialize variables from command line
    for (int x = 0;x < NUMBER_OF_RESOURCES;x++){
        available[x] = atoi(argv[x+1]);
    }

    //initialize file 
    FILE *fp = fopen("to_read.txt", "r");
    if (fp == NULL){
        perror("Error opening file.\n");
        return 1;
    }

    char line[100];
    //read maximum demand from file
    for (int x = 0; x<NUMBER_OF_CUSTOMERS;x++){
        if (fgets(line, sizeof(line), fp) == NULL) {
            printf("Error reading line for customer %d\n", x);
            fclose(fp);
            return 1;
        }

        //parse line
        if (sscanf(line, "%d,%d,%d,%d",
                &maximum[x][0], &maximum[x][1],
                &maximum[x][2], &maximum[x][3]) != NUMBER_OF_RESOURCES) {
            printf("Invalid input format at customer %d\n", x);
            fclose(fp);
            return 1;
        }

        // Initialize allocation and need
        for (int y = 0; y < NUMBER_OF_RESOURCES; y++) {
            allocation[x][y] = 0;
            need[x][y] = maximum[x][y];
        }
    }

    fclose(fp);

    //user input loop
    char input[100];
    while (1){
        printf("\nEnter command (RQ/RL/*/QUIT): ");
        fgets(input, sizeof(input),stdin);

        char command[3];
        int customer_num, resources[NUMBER_OF_RESOURCES];
        int count = sscanf(input, "%2s %d %d %d %d %d", command, &customer_num, &resources[0], &resources[1], &resources[2], &resources[3]);
        
        //request command
        if (strcmp(command, "RQ") == 0 && count == 6) {
            if (customer_num < 0 || customer_num >= NUMBER_OF_CUSTOMERS) {
                printf("Invalid customer number.\n");
                continue;
            }
            else if (request_resources(customer_num, resources) == 0) {
                printf("Request granted\n");
            } 
            else {
                printf("Request denied (unsafe state)\n");
            }
        } 
        //release command
        else if (strcmp(command, "RL") == 0 && count == 6) {
            release_resources(customer_num, resources);
            printf("Resources released\n");
        } 
        //print state command
        else if (strcmp(command, "*") == 0) {
            print_state();
        } 
        //quit command
        else if (strncmp(input, "QUIT", 4) == 0) {
            break;
        } 
        //invalid command
        else {
            printf("Invalid command or wrong number of arguments\n");
        }
    }

    return 0;
    
}