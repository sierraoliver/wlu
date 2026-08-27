/**
 * -------------------------------------
 * @file  by_ptr.c
 * Lab 2 Pointer Functions Source Code File
 * -------------------------------------
 * @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
 *
 * @version 2025-01-06
 *
 * -------------------------------------
 */
#include "by_ptr.h"

void fill_values_by_ptr(int *values, int size) {

    for(int i = 0; i < size; i++) {
        *(values + i) = i + 1;
    }
}

void fill_squares_by_ptr(int *values, long int *squares, int size) {

    for (int x = 0;x<size;x++){
        *(squares+x) = values[x] * values[x];
    }    

}

void print_by_ptr(int *values, long int *squares, int size) {

    printf("Value  Square    \n");
    printf("-----  ----------\n");

    for (int x = 0;x<size;x++){
        printf("%5d  %10ld\n",*(values+x),*(squares+x));
    }

}
