/**
 * -------------------------------------
 * @file  functions.c
 * Lab 2 Functions Source Code File
 * -------------------------------------
 * @author Sierra Oliver, 169067437, oliv7437@mylaurier.c
 *
 * @version 2025-01-06
 *
 * -------------------------------------
 */
#include "functions.h"
#include <ctype.h>

int sum_three_integers(void) {
    char str [100];
    char *line = str;
    int number;
    int sum = 0;
    int check;

    do{
        number = '\0';
        check = 0;
        printf("Enter three comma-separated integers: ");
        gets (line);
        while (check <3|| *line!='\0'){
            if(!isdigit(*line) && *line!= ','){
                number = '\0';
                break;
            }
            else if (*line != ',' && check !=3){
                check++;
                while (isdigit(*line)){
                    number += *line;
                    line++;
                }
                sum += (number-'0');
                number = '\0';
            }
            else{
                line++;
            }
        }
    
        if (check<3){
            printf("The integers were not properly entered.\n");
            sum = 0;
        }

    }while (check <3);

    return sum;

}
