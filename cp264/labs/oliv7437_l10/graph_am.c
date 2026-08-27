/**
 * -------------------------------------
 * @file  graph_am.c
 * Adjacency Matrix Graph Code File
 * -------------------------------------
 * @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
 *
 * @version 2025-01-06
 *
 * -------------------------------------
 */
#include "graph_am.h"

// Initializes an adjacency matrix graph.
graph_am* graph_am_initialize(int size) {
    graph_am *source = malloc(sizeof *source);
    source->size = size;
    // Initialize values to zeroes.
    source->values = calloc(size * size, sizeof *source->values);
    return source;
}

void graph_am_free(graph_am **source) {
    // Free up the data array.
    free((*source)->values);
    (*source)->values = NULL;
    free(*source);
    *source = NULL;
    return;
}

int graph_am_add_vertice(graph_am *source, const graph_am_pair *pair) {
    int added = 0;

    if ((pair->row >=0 || pair->row < source->size) && (pair->col >=0 ||pair->col < source->size)){
        if (pair->row == pair->col){
            source->values[pair->row*source->size+pair->col] = 2;
        }
        else{
            source->values[pair->row*source->size+pair->col]=1;
            source->values[pair->col*source->size+pair->row]=1;
        }
        added=1; 
    }

    return added;
}

int graph_am_remove_vertice(graph_am *source, const graph_am_pair *pair) {
    int removed = 0;

    if ((pair->row >=0 || pair->row < source->size) && (pair->col >=0 || pair->col < source->size)){
            source->values[pair->row*source->size+pair->col]=0;
            source->values[pair->col*source->size+pair->row]=0;
            removed = 1;
    }

    return removed;
}

graph_am* graph_am_create(int size, const graph_am_pair pairs[], int count) {
    graph_am *source = graph_am_initialize(size);
    
    for (int x = 0;x<count;x++){
        graph_am_add_vertice(source, &pairs[x]);
    }

    return source;
}

void graph_am_neighbours(const graph_am *source, int vertex, int vertices[], int *count) {
    int *ptr = vertices;
    for (int x = (*count); x<source->size;x++){
        int value = source->values[vertex*source->size+x];
        if (value >0){
            *(ptr+(*count)) = x;
            (*count) +=1;
        }
    }
    return;
}

int graph_am_degree(const graph_am *source, int vertex) {
    int connected = 0;
    for (int x = 0; x<source->size;x++){
        int value = source->values[vertex*source->size+x];
        connected +=value;
    }

    return connected;
}

void graph_am_breadth_traversal(const graph_am *source, int vertex, int vertices[], int *count) {
    int visited [source->size];
    for (int x = 0;x<source->size;x++){
        visited[x] = 0;
    }
    int *ptr = vertices;
    *(ptr + (*count)) = vertex;
    (*count) ++;
    visited[vertex] = 1;

    int neighbour_count = 0;
    int neighbour_vertices [source->size];
    graph_am_neighbours(source, vertex, neighbour_vertices, &neighbour_count);
    for (int x = 0; x< neighbour_count;x++){
        if (!visited[neighbour_vertices[x]]){
            *(ptr + (*count)) = neighbour_vertices[x];
            (*count) ++;
            visited[x] = 1;
            graph_am_neighbours(source,neighbour_vertices[x], neighbour_vertices, &neighbour_count);
        }
        
    }
    return;
}

void graph_am_depth_traversal_aux (const graph_am *source, int vertex, int visited[], int *ptr, int *count){
    int neighbour_count = 0;
    int neighbour_vertices[source->size];
    graph_am_neighbours(source, vertex, neighbour_vertices, &neighbour_count);

    for (int x = neighbour_count-1; x >=0; x--) {
        int neighbor = neighbour_vertices[x];
        if (!visited[neighbor]) {  
            visited[neighbor] = 1;  
            *(ptr + (*count)) = neighbor; 
            (*count)++;
            graph_am_depth_traversal_aux(source, neighbor, visited, ptr, count); 
        }
    }
}

void graph_am_depth_traversal(const graph_am *source, int vertex, int vertices[], int *count) {
    int visited [source->size];
    for (int x = 0;x<source->size;x++){
        visited[x] = 0;
    }
    int *ptr = vertices;
    *(ptr + (*count)) = vertex;
    (*count) ++;
    visited[vertex] = 1;

    graph_am_depth_traversal_aux (source, vertex, visited, ptr, count);

    return;
}

// Prints the contents of an adjacency matrix graph.
void graph_am_print(const graph_am *source) {
    // Print the column numbers.
    printf("    ");

    for(int i = 0; i < source->size; i++)
        printf("%3d", i);
    printf("\n");
    printf("    ");
    for(int i = 0; i < source->size; i++)
        printf("---");
    printf("\n");

    // Print the row numbers and rows.
    for(int i = 0; i < source->size; i++) {
        printf("%3d|", i);

        for(int j = 0; j < source->size; j++) {
            // find item using offsets
            printf("%3d", *(source->values + i * source->size + j));
        }
        printf("\n");
    }
}
