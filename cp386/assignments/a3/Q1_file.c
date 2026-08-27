/**
* -------------------------------------
* @file Q1_file.c
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
#include <pthread.h>
#include <string.h>

typedef struct{
    int row;
    int col;
} parameters;

//global variables
int sudoku_num[9][9];
int valid[27] = {0};

void file_read (FILE *ptr){
    for (int x = 0; x<9;x++){
        for (int y = 0; y<9;y++){
            fscanf(ptr,"%d", &sudoku_num[x][y]);
        }
    }
    fclose(ptr);
    return;
}

void *check_row (void *arg){
    parameters *p = (parameters*) arg;
    int row = p->row;
    int digits [9] = {0};
    int value;

    for (int x = 0;x<9;x++){
        value = sudoku_num[row][x];
        if ((value>=1 && value<=9)&& digits[value-1]==0){
            digits[num-1] = 1;
        }
        else{
            pthread_exit(NULL);
        }
    }

    valid[row] = 1;
    pthread_exit (NULL);
}

void *check_col (void *arg){
    parameters *p = (parameters*) arg;
    int col = p->col;
    int digits [9] = {0};
    int value;

    for (int x = 0;x<9;x++){
        value = sudoku_num[x][col];
        if ((value>=1 && value<=9)&& digits[value-1]==0){
            digits[num-1] = 1;
        }
        else{
            pthread_exit(NULL);
        }
    }

    valid[9+col] = 1;
    pthread_exit (NULL);
}

void *check_subgrid (void *arg){
    parameters *p = (parameters*) arg;
    int start_row = p->row;
    int start_col = p->col;
    int digits [9] = {0};
    int value;

    for (int x = start_row; x<start_row +3; x++){
        for (int y = start_col; y<start_col + 3; y++){
            value = sudoku_num[x][y];
            if ((value>=1 && value<=9)&& digits[value-1]==0){
                digits[num-1] = 1;
            }
            else{
                pthread_exit(NULL);
            }
        }
    }
    valid[18+(start_row/3)*3+(start_col/3)] = 1;
    pthread_exit (NULL);
}

int main(int argc, char *argv[]){
    if (argc == 0){
        fprintf(stderr, "Enter a file to check sudoku puzzle\n");
        return 1;
    }

    char *file_name;
    FILE *ptr;

    file_name = argv[0];

    ptr = fopen(file_name, "r");
    if (ptr == NULL){
        perror("File open failed");
        return 1;
    }

    file_read (ptr);

    pthread_t threads [27];
    int thread_index = 0;

    //create row threads
    for (int x = 0; x<9;x++){
        parameters *data = (parameters*) malloc (sizeof(parameters));
        data->row = x;
        data->col = 0;
        pthread_create (&threads[thread_index],NULL, check_row,data);
        thread_index ++;
    }

    //create col threads
    for (int x = 0; x<9;x++){
        parameters *data = (parameters*) malloc (sizeof(parameters));
        data->row = 0;
        data->col = x;
        pthread_create (&threads[thread_index],NULL, check_col,data);
        thread_index ++;
    }

    //create subgrid threads
    for (int x = 0; x<9;x+=3){
        for (int y = 0; y<9;y+=3){
            parameters *data = (parameters*) malloc (sizeof(parameters));
            data->row = x;
            data->col = y;
            pthread_create (&threads[thread_index],NULL, check_subgrid,data);
            thread_index ++;
        }
    }

    //wait for all threads to finish
    for (int x = 0; x<27;x++){
        pthread_join(threads[x], NULL);
    }

    //validate all regions
    for (int x = 0;x<27;x++){
        if (valid[x] == 0){
            printf("Not a Valid Sudoku Puzzle\n");
            return 0;
        }
    }

    printf("Valid Sudoku Puzzle");
    return 0;

}