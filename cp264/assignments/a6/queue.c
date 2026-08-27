/**
* -------------------------------------
* @file queue.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-02-27)}
*
* -------------------------------------
*/

#include <stdio.h>
#include "queue.h"

void enqueue(QUEUE *qp, NODE *np) {
    if (np != NULL){
        if (qp->length == 0){
            qp->front = np;
            qp->rear = np;
        }
        else if (qp->length == 1){
            qp->front->next = np;
            qp->rear = np;
        }
        else{
            qp->rear->next = np;
            qp->rear = np;
        }
        qp->length+=1;
    }
}  

NODE *dequeue(QUEUE *qp) {
    NODE *remove = NULL;

    if (qp->length >0){
        remove = qp->front;
        if (qp->length == 1){
            qp->front = NULL;
            qp->rear = NULL;
        }
        else{
            qp->front = qp->front->next;
        }
        remove->next = NULL;
        qp->length-=1;
    }

    return remove;
}

void clean_queue(QUEUE *qp) {
  clean(&(qp->front));
  qp->front = NULL;
  qp->rear = NULL;
  qp->length=0;
}