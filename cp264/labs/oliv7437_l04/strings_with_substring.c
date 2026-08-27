/**
 * -------------------------------------
 * @file  strings_with_substring.c
 * Lab 4 Source Code File
 * -------------------------------------
 * @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
 *
 * @version 2025-01-06
 *
 * -------------------------------------
 */
#include "functions.h"

void strings_with_substring(strings_array *data, char *substr) {

    for (int x = 0;x<data -> lines;x++){
        char *token = strstr(data -> strings[x],substr);
        if (token != NULL){
            printf("%s\n",data->strings[x]);
        }
    }

}
