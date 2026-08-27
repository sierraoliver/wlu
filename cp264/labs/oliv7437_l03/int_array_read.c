/**
 * -------------------------------------
 * @file  int_array_read.c
 * Lab 3 Source Code File
 * -------------------------------------
 * @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
 *
 * @version 2025-01-06
 *
 * -------------------------------------
 */
#include "functions.h"
#include <ctype.h>

void int_array_read(int *array, int size) {
    char str[100];
    char *line = str;
    int check=0;
    int number;
    char sign;

    printf("Enter %d values for an array of int.\n", size);

    while (check !=size){
        number = '\0';
        sign = '\0';
        printf("Value for index %d:", check);
        gets (line);

        if (*line == '-'){
            sign +=*line;
            line++;
        }

        if (isdigit(*line)){
            sscanf(line,"%d",&number);
            if (sign == '-'){
                array[check] = (number) *-1;
            }
            else{
                array[check] = number;
            }
            check++;
        }
        else{
            printf("Not a valid integer\n");
        }
    }   

}
