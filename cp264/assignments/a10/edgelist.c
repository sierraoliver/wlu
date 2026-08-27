/**
* -------------------------------------
* @file edgelist.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-03-31)}
*
* -------------------------------------
*/

#include <stdio.h>
#include <stdlib.h> 
#include "edgelist.h"

EDGELIST *new_edgelist() {
    EDGELIST *tp = malloc(sizeof(EDGELIST));
    tp->size = 0;
    tp->start = NULL;
    tp->end = NULL;
    return tp;
}

void insert_edge_end(EDGELIST *g, int from, int to, int weight) {
    EDGENODE *new = malloc (sizeof(EDGENODE));
    new-> from = from;
    new->to = to;
    new->weight = weight;
    new->next = NULL;
    if (g->size == 0){
        g->start = new;
        g->end = new; 
    }
    else{
        g->end->next = new;
        g->end = new;
    }
    g->size +=1;
}

void insert_edge_start(EDGELIST *g, int from, int to, int weight) {
    EDGENODE *new = malloc (sizeof(EDGENODE));
    new-> from = from;
    new->to = to;
    new->weight = weight;
    new->next = NULL;
    if (g->size == 0){
        g->start = new;
        g->end = new; 
    } 
    else{
        new->next = g->start;
        g->start = new;
    }
    g->size +=1;
}

void delete_edge(EDGELIST *g, int from, int to) {
    EDGENODE *prev;
    EDGENODE *current = g->start;
    while ((current->from != from) && (current->to != to)){
        prev = current;
        current = current->next;
        if (current == NULL){
            return;
        }
    }
    if(g->size == 1){
        g->start = NULL;
        g->end = NULL;
    }
    else if (prev == NULL){
        g->start = g->start->next;
    }
    else if (current->next == NULL){
        prev->next = current->next;
        g->end = prev;
    }
    else{
        prev->next = current->next;
    }
    g->size-=1;
    free(current);
    

}

int weight_edgelist(EDGELIST *g) {
    EDGENODE *current = g->start;
    int total = 0;

    while (current != NULL){
        total += current->weight;
        current = current->next;
    }

    return total;
}

void clean_edgelist(EDGELIST **gp) {
    EDGELIST *g = *gp;
    EDGENODE *temp, *p = g->start;
    while (p) {
        temp = p;
        p = p->next;
        free(temp);
    }
    free(g);
    *gp = NULL;
}

void display_edgelist(EDGELIST *g) {
    if (g == NULL)
        return;
    printf("size %d ", g->size);
    printf("(from to weight) ");
    EDGENODE *p = g->start;
    while (p) {
        printf("(%d %d %d) ", p->from, p->to, p->weight);
        p = p->next;
    }
}
