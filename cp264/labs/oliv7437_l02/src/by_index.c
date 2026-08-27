/**
 * -------------------------------------
 * @file  by_index.c
 * Lab 2 Index Functions Source Code File
 * -------------------------------------
 * @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
 *
 * @version 2025-01-06
 *
 * -------------------------------------
 */
#include "by_index.h"

void fill_values_by_index(int values[], int size) {

    for(int i = 0; i < size; i++) {
        values[i] = i + 1;
    }
}

void fill_squares_by_index(int values[], long int squares[], int size) {

    for (int x = 0;x < size;x++){
        int number = values[x];
        squares[x] = number*number;
    }

}

void print_by_index(int values[], long int squares[], int size) {

    printf("Value  Square    \n");
    printf("-----  ----------\n");

    for (int x = 0;x<size;x++){
        printf("%5d  %10ld\n",values[x],squares[x]);
    }

}