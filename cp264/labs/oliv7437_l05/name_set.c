/**
 * -------------------------------------
 * @file  name_set_initialize.c
 * Lab 5 Source Code File
 * -------------------------------------
 * @author Heider Ali, 999999999, heali@wlu.ca
 * @author David Brown, 123456789, dbrown@wlu.ca
 *
 * @version 2025-01-06
 *
 * -------------------------------------
 */
#include "name_set.h"

name_set* name_set_initialize() {
    // Allocate memory to the data structure
    name_set *set = malloc(sizeof *set);
    // Initialize the header fields.
    set->front = NULL;
    set->rear = NULL;
    return set;
}

int name_set_free(name_set **set) {
    int count = 0;
    name_set_node *current = (*set)->front;

    while (current != NULL){
        (*set)->front = current->next;
        current = current->next;
        free (current);
        count++;
    }
    free ((*set)->front);
    count++;

    return count;

}

BOOLEAN name_set_append(name_set *set, const char *first_name, const char *last_name) {
    BOOLEAN append = FALSE;

    if (name_set_contains(set, first_name, last_name) == FALSE){
        name_set_node *new = (name_set_node*) malloc(sizeof(name_set_node));
        strcpy(new->first_name,first_name);
        strcpy(new->last_name, last_name);
        new->next = NULL;

        if (set->front == NULL){
            set->front= new;
            set->rear = new;
        }
        else if (set->front == set->rear){
            set->front->next = new;
            set->rear = new;
        }
        else{
            name_set_node *temp = set->rear;
            set->rear = new;
            temp->next = new;
        }
        append = TRUE;

    }

    return append;
}

BOOLEAN name_set_contains(const name_set *set, const char *first_name, const char *last_name) {
    BOOLEAN contains = FALSE;
    int first;
    int last;

    name_set_node *current = set->front;
    while (current != NULL){
        first = 1;
        last = 1;

        char *f_ptr = current->first_name;
        if (strlen(f_ptr) == strlen(first_name)){
            for (int x = 0; x<strlen(f_ptr);x++){
                if (*(f_ptr +x) != *(first_name+x)){
                    first = 0;
                    break;
                }
            }
        } 
        else{
            first = 0;
        }

        char *l_ptr = current->last_name;
        if (strlen(l_ptr) == strlen(last_name)){
            for (int x = 0; x<strlen(l_ptr);x++){
                if (*(l_ptr +x) != *(last_name+x)){
                    last = 0;
                    break;
                }
            }
        } 
        else{
            last = 0;
        }
        
        if (first ==1 && last ==1){
            return TRUE;
        }
        current = current->next;
    }

    return contains;

}

void name_set_print(const name_set *set) {
    name_set_node *current = set->front;

    while (current != NULL){
        printf("%s, %s\n",current->last_name, current->first_name);
        current = current->next;
    }

}
