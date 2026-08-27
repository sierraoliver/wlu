/**
* -------------------------------------
* @file graph.c
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
#include <string.h>
#include "queue_stack.h"
#include "graph.h"

GRAPH *new_graph(int order) {
  GRAPH *gp = malloc(sizeof(GRAPH));
  gp->nodes = malloc(order * sizeof(GNODE*));
  
  int i;
  for (i = 0; i < order; i++) {
    gp->nodes[i] = malloc(sizeof(GNODE));
    gp->nodes[i]->nid = i;
    strcpy(gp->nodes[i]->name, "null");
    gp->nodes[i]->neighbor = NULL;
  }
  
  gp->order = order;
  gp->size = 0;  
 
  return gp;
}

void insert_edge_graph(GRAPH *g, int from, int to, int weight) {
    int found = 0;
    ADJNODE *ptr = g->nodes[from]->neighbor;
    if (ptr){
        while (ptr->next){
            if (ptr->nid == to){
                found = 1;
                break;
            }        
            ptr = ptr->next;
        }
        if (ptr->nid == to){
            found = 1;
        }
        if (found){
            ptr->weight = weight;
        }
        else{
            ADJNODE *adj = malloc(sizeof(ADJNODE));
            adj->nid = to;
            adj->weight = weight;
            adj->next = NULL;
            ptr->next = adj;
        }
    }
    else{
        ADJNODE *adj = malloc(sizeof(ADJNODE));
        adj->nid = to;
        adj->weight = weight;
        adj->next = NULL;
        g->nodes[from]->neighbor = adj;
    }
   
    g->size+=1;
    
}

void delete_edge_graph(GRAPH *g, int from, int to) {
    ADJNODE *ptr;
    ADJNODE *prev = NULL;
    for (int i = 0; i < g->order; i++) {
        ptr = g->nodes[i]->neighbor;
        while (ptr != NULL) {
            if (i == from && ptr->nid == to){
                if (prev != NULL){
                    prev->next = ptr->next;
                }
                else{
                    GNODE *new = malloc(sizeof(GNODE));
                    new->nid = from;
                    new->neighbor = ptr->next;
                    g->nodes[from]= new;
                }
                g->size-=1;
                free(ptr);
                return;
            }     
            prev = ptr;   
            ptr = ptr->next;
        }
    }

}

int get_edge_weight(GRAPH *g, int from, int to) {
    ADJNODE *ptr;
    if (g){
        for (int i = 0; i < g->order; i++) {
            ptr = g->nodes[i]->neighbor;
            while (ptr != NULL) {
                if (i == from && ptr->nid == to){
                    return ptr->weight;
                }  
                ptr = ptr->next;
            }
        }
    }
    return INFINITY;
}

void traverse_bforder(GRAPH *g, int nid) {
    if (g == NULL) return;

    int n = g->order;
    int visited[n];

    for (int i = 0; i<n; i++){
        visited[i] = 0;
    }

    QUEUE queue = {0};
    GNODE *node = NULL;
    ADJNODE *adj = NULL;
    enqueue (&queue, g->nodes[nid]);
    visited[nid] = 1;
    while (queue.front){
        node = (GNODE*) dequeue (&queue);
        printf("(%d %s) ", node->nid, node->name);
        adj = node->neighbor;
        while (adj){
            if (visited[adj->nid] == 0){
                enqueue (&queue, g->nodes[adj->nid]);
                visited[adj->nid] = 1;
            }
            adj = adj->next;
        }
    }
    clean_queue(&queue);
}


// Use auxiliary stack data structure for the algorithm
void traverse_dforder(GRAPH *g, int nid) {
    if (g == NULL) return;

    int n = g->order;
    int visited[n];

    for (int i = 0; i<n; i++){
        visited[i] = 0;
    }

    STACK stack = {0};
    GNODE *node = NULL;
    ADJNODE *adj = NULL;
    push (&stack, g->nodes[nid]);
    visited[nid] = 1;
    while (stack.top){
        node = (GNODE*) pop (&stack);
        printf("(%d %s) ", node->nid, node->name);
        adj = node->neighbor;
        while (adj){
            if (visited[adj->nid] == 0){
                push(&stack, g->nodes[adj->nid]);
                visited[adj->nid] = 1;
            }
            adj = adj->next;
        }
    }
    clean_stack(&stack);
}

void clean_graph(GRAPH **gp) {
  int i;
  GRAPH *g = *gp;
  ADJNODE *temp, *ptr;
  for (i = 0; i < g->order; i++) {
    ptr = g->nodes[i]->neighbor;
    while (ptr != NULL) {
      temp = ptr;
      ptr = ptr->next;
      free(temp);
    }
    free(g->nodes[i]);
  }
  free(g->nodes);
  free(g);
  *gp = NULL;
}

void display_graph(GRAPH *g) {
  if (g ) {
  printf("order %d ", g->order);
  printf("size %d ", g->size);
  printf("(from to weight) ");
  int i;
  ADJNODE *ptr;
  for (i = 0; i < g->order; i++) {
    //printf("\n%d:", g->nodes[i]->nid);
    ptr = g->nodes[i]->neighbor;
    while (ptr != NULL) {
      printf("(%d %d %d) ", i,  ptr->nid, ptr->weight);
      ptr = ptr->next;
    }
  }
  }
}
