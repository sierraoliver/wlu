/**
* -------------------------------------
* @file hash.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-03-21)}
*
* -------------------------------------
*/

#include <stdio.h>
#include <stdlib.h> 
#include <string.h>
#include "hash.h"

HNODE *hashtable_search(HASHTABLE *ht, char *name) {
    int i = hash(name, ht->size);
    HNODE *p = ht->hna[i];
    while (p){
        if (strcmp(p->data.name, name)==0){
            break;
        }
        p = p->next;
    }
    return p;
}

int hashtable_insert(HASHTABLE *ht, DATA data) {
    int i = hash(data.name, ht->size);
    HNODE *p = ht->hna[i];
    HNODE *prev = NULL;
    while (p){
        if (strcmp(p->data.name, data.name)==0){
            p->data.value = data.value;
            return 0;
        }
        prev = p;
        p = p->next;
    }
    HNODE *new = (HNODE*) malloc (sizeof(HNODE));
    new->next = NULL;
    strcpy(new->data.name, data.name);
    new->data.value = data.value;
    if (prev == NULL){
        ht->hna[i] = new;
    }
    else{
        prev->next = new;
    }
    ht->count +=1;
    return 1;
}

int hashtable_delete(HASHTABLE *ht, char *name) {
    int i = hash(name, ht->size);
    HNODE *p = ht->hna[i];
    HNODE *prev = NULL;
    while (p){
        if (strcmp(p->data.name, name)==0){
            if (prev){
                prev->next = p->next;
            }
            else{
                ht->hna[i] = p->next;
            }
            free(p);
            ht->count-=1;
            return 1;
        }
        else{
            prev = p;
            p = p->next;
        }
        
    }
    return 0;
}

int hash(char* key, int size) {
    unsigned int hash = 0;
    while (*key) {
        hash += *key++;
    }
    return hash % size;
}

HASHTABLE *new_hashtable(int size) {
    HASHTABLE *ht = (HASHTABLE*) malloc(sizeof(HASHTABLE));
    ht->hna = (HNODE**) malloc(sizeof(HNODE**) * size);
    int i;
    for (i = 0; i < size; i++)
        *(ht->hna + i) = NULL;

    ht->size = size;
    ht->count = 0;
    return ht;
}


void hashtable_clean(HASHTABLE **htp) {
    if (*htp == NULL)
        return;
    HASHTABLE *ht = *htp;
    HNODE *p, *temp;
    int i;
    for (i = 0; i < ht->size; i++) {
        p = ht->hna[i];
        while (p) {
            temp = p;
            p = p->next;
            free(temp);
        }
        ht->hna[i] = NULL;
    }
    free(ht->hna);
    ht->hna = NULL;
    *htp = NULL;
}
