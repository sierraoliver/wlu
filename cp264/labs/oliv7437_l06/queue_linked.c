/**
 * -------------------------------------
 * @file  queue_linked.c
 * Linked Queue Source Code File
 * -------------------------------------
 * @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
 *
 * @version 2025-01-06
 *
 * -------------------------------------
 */
// Includes
#include "queue_linked.h"

// Functions

queue_linked* queue_initialize() {
    queue_linked *source = malloc(sizeof *source);

    source->front = NULL;
    source->rear = NULL;
    source->count = 0;

    return source;
}

void queue_free(queue_linked **source) {

    queue_node *node;

    while ((*source)->front != NULL){
        node = (*source)->front;
        (*source)->front = (*source)->front->next;
        free(node);
    }

    free(*source);
    *source = NULL;

    return;
}

bool queue_empty(const queue_linked *source) {
    bool empty = false;

    if (source->count == 0){
        empty = true;
    }

    return empty;
}

int queue_count(const queue_linked *source) {

    return source->count;
}

bool queue_insert(queue_linked *source, data_ptr item) {
    bool insert = true;

    queue_node *new = malloc(sizeof *new);
    new->item = malloc(sizeof *new->item);
    data_copy(new->item, item);
    new->next = NULL;

    if (source->count == 0){
        source-> front = new;
        source-> rear = new;
    }
    else if (source->count ==1){
        source->front->next = new;
        source->rear = new;
    }
    else{
        source->rear->next = new;
        source->rear = new;
    }
    source->count +=1;

    return insert;
}

bool queue_peek(const queue_linked *source, data_ptr item) {
    bool peek = false;

    if (source->front !=NULL){
        data_copy(item, source->front->item);
        peek = true;
    }

    return peek;
}

bool queue_remove(queue_linked *source, data_ptr *item) {
    bool remove = false;

    if (source->front != NULL){
        remove = true;
        *item = source->front->item;
        queue_node *node = source->front;

        if (source->count == 1){
            source->front = NULL;
            source->rear = NULL;
        }
        else{
            source->front = source->front->next;
        }
        free (node);
        source->count-=1;
        
    }

    return remove;
}

void queue_print(const queue_linked *source) {
    char string[DATA_STRING_SIZE];
    queue_node *current = source->front;

    while(current != NULL) {
        data_string(string, sizeof string, current->item);
        printf("%s\n", string);
        current = current->next;
    }
    return;
}
