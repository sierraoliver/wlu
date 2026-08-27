/**
* -------------------------------------
* @file myrecord_sllist.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-02-14)}
*
* -------------------------------------
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "myrecord_sllist.h"

/**
 * Search singly linked list by the key name.
 * 
 * @param SLL *sllp - provides the address of a singly linked list structure.
 * @param char *name - key to search
 * @return Pointer to found node if found; otherwise NULL
 */
 NODE *sll_search(SLL *sllp, char *name){
    NODE *current = sllp->start;
    
    while (current != NULL){
        if (strcmp(current->data.name,name)==0){
            return current;
        }
        current = current->next;    
    }
    
    return current;
 }

 /**
  * Insert a new record to linked list at the position sorted by record name field.
  *
  * @param SLL *sllp - provides the address of a singly linked list structure.
  * @param char *name - name field of the new record.
  * @param float score - the score data of the new record.
  */
 void sll_insert(SLL *sllp, char *name, float score){
    NODE *new = (NODE*) malloc (sizeof(NODE));
    strcpy(new->data.name, name);
    new->data.score = score;
    new->next = NULL;

    if (sllp->start == NULL){
        sllp->start = new;
        sllp->length+=1;
        return;
    }

    NODE *prev = NULL, *current = sllp->start;
    while (current != NULL){
        if (strcmp(current->data.name, name)>=0){
            break;
        }
        prev = current;
        current = current->next;
    }

    if (prev == NULL){
        new->next = sllp->start;
        sllp->start = new;
    }
    else{
        prev->next = new;
        new->next = current;
    }

    sllp->length+=1;

 }
 
 /**
  * Delete a node of record matched by the name key from linked list.
  * 
  * @param SLL *sllp provides the address of a singly linked list structure.
  * @param name - key used to find the node for deletion. 
  * @return 1 if deleted a matched node, 0 otherwise. 
  */
 int sll_delete(SLL *sllp,  char *name){
    int delete = 0;
    NODE *prev = NULL, *current = sllp->start;

    while (current != NULL){
        if (strcmp(current->data.name, name)==0){
            delete = 1;
            break;
        }
        prev = current;
        current = current->next;
    }

    if (delete==1){
        if (prev == NULL){
            sllp->start = current->next;
        }
        else{
            prev->next = current->next;
        }
        sllp->length -=1;
    }

    return delete;

 }
 
 /**
  * Clean singly linked list, delete all nodes. 
  * @param @param SLL *sllp provides the address of a singly linked list structure.
  */
 void sll_clean(SLL *sllp){
    NODE *temp, *ptr = sllp->start;
    while (ptr != NULL) {
        temp = ptr;
        ptr = ptr->next;
        free(temp);
    }
    sllp->start = NULL;
    sllp->length = 0;
 }