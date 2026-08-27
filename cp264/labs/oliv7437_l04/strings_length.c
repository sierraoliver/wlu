/**
 * -------------------------------------
 * @file  strings_length.c
 * Lab 4 Source Code File
 * -------------------------------------
 * @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
 *
 * @version 2025-01-06
 *
 * -------------------------------------
 */
#include "functions.h"

void strings_length(strings_array *data, FILE *fp_short, FILE *fp_long, int length) {
    for (int x = 0; x<data->lines;x++){
        int size = strlen(data->strings[x]);
        if (size < length){
            fprintf(fp_short,"%s\n",data->strings[x]);
        }
        else{
            fprintf(fp_long, "%s\n",data->strings[x]);
        }
    }

}
