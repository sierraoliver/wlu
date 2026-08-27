/**
* -------------------------------------
* @file dllist.c
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
#include "dllist.h"

/*
 * Create and return a new node using malloc() with passed data value and returns pointer of the node.
*/
NODE *dll_node(char value){
    NODE *new = (NODE*) malloc(sizeof(NODE));

    new -> data = value;
    new -> prev = NULL;
    new -> next = NULL;

    return new;
}

/*
 * Insert a given node at the beginning the of a doubly linked list. 
 * @param DLL *dllp -  reference to input DLL variable 
 * @param NODE *np  -  reference of a NODE node to be inserted
*/
void dll_insert_start(DLL *dllp, NODE *np){
    if (dllp->start == NULL && dllp->end == NULL){
        dllp->start = np;
        dllp->end= np;
    }
    else{
        np->next = dllp->start;
        dllp->start->prev = np;
        dllp->start = np;
    }

    dllp->length+=1;
}

/*
 * Insert a node at the end of a doubly linked list.
 * @param DLL *dllp -  reference to input DLL variable 
 * @param NODE *np  -  reference of a NODE node to be inserted
*/
void dll_insert_end(DLL *dllp, NODE *np){
    if (dllp->start == NULL && dllp->end == NULL){
        dllp->start = np;
        dllp->end= np;
    }
    else{
        np->prev = dllp->end;
        dllp->end->next = np;
        dllp->end = np;
    }

    dllp->length+=1;
}

/*
 * This deletes the first node of a doubly linked list.
 * @param DLL *dllp -  reference to input DLL variable 
*/
void dll_delete_start(DLL *dllp){
    NODE *front = dllp->start;
    if (front != NULL){
        if (dllp->length == 1){
            dllp->start = NULL;
            dllp->end = NULL;
        }
        else{
            NODE *new_front = dllp->start->next;
            dllp->start = new_front;
            new_front->prev = NULL;
        }
        free (front);
        dllp->length-=1;
    }
    
}

/*
 * Delete the end node of a doubly linked list.
 * @param DLL *dllp -  reference to input DLL variable  
*/
void dll_delete_end(DLL *dllp){
    NODE *back = dllp->end;
    if (back != NULL){
        if (dllp->length == 1){
            dllp->start = NULL;
            dllp->end = NULL;
        }
        else{
            NODE *new_back = dllp->end->prev;
            dllp->end = new_back;
            new_back->next = NULL;
        }
        free(back);
        dllp->length-=1;
    }
}

/*
 * Clean and free the nodes of a doubly linked list and reset start and length.
 * @param DLL *dllp -  reference to input DLL variable 
*/
void dll_clean(DLL *dllp){
    NODE *temp, *current = dllp->start;

    while (current!= NULL){
        temp = current;
        current = current->next;
        free (temp);
    }
    dllp->start = NULL;
    dllp->end = NULL;
    dllp->length = 0;

}