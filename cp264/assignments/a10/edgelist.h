/**
* -------------------------------------
* @file edgelist.h
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-03-31)}
*
* -------------------------------------
*/

#ifndef EDGELIST_H
#define EDGELIST_H

typedef struct edgenode {
  int from;
  int to;
  int weight;
  struct edgenode *next;
} EDGENODE;


typedef struct edgelist {
  int size;    
  EDGENODE *start;
  EDGENODE *end;
} EDGELIST;

/* Create and return a new edge list graph*/
EDGELIST *new_edgelist();

/* Add a new edge at the start of the linked list of edges*/
void insert_edge_start(EDGELIST *g, int from, int to, int weight);

/* Add an new edge at the end of the linked list of edges */
void insert_edge_end(EDGELIST *g, int from, int to, int weight);

/* Delete edge (from to) from the edgelist */
void delete_edge(EDGELIST *g, int from, int to);

/* Get the weight of the graph */
int weight_edgelist(EDGELIST *g);

/* clean the graph by free all dynamically allocated memory*/
void clean_edgelist(EDGELIST **gp);

/* Display edge list graph*/
void display_edgelist(EDGELIST *g);

#endif