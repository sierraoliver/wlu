/**
 * -------------------------------------
 * @file  sum_integers.c
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

int sum_integers(void) {
    char str [100];
    char *line = str;
    char number;
    int result;
    int sum = 0;

     printf("Enter integers, one per line:\n");

    do{
        number = '\0';
        result = '\0';

        gets (line);
        while (*line != '\0'){
            if (isdigit(*line)){
                number +=*line;
                sscanf(line,"%d",&result);
                sum+= (result);
            }
            break;
        }
        
        
    }while (isdigit(number));
    
    return sum;

}
