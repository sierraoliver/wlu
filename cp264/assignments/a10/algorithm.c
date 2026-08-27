/**
* -------------------------------------
* @file algorithm.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-04-01)}
*
* -------------------------------------
*/

#include <stdio.h>
#include <stdlib.h> 
#include "heap.h"
#include "algorithm.h"

EDGELIST *mst_prim(GRAPH *g, int start) {
    if (g == NULL) return NULL;
    int heapindex, u, n = g->order, T[n], parent[n];
    for (int i = 0; i < n; i++){
        T[i] = 0; 
        parent[i] = -1;
    }

    HEAPDATA hn; 
    HEAP *h = new_heap(4); 

    T[start] = 1;
    ADJNODE *temp = g->nodes[start]->neighbor;
    while (temp != NULL) {
        hn.key = temp->weight;
        hn.value = temp->nid;
        heap_insert(h, hn);
        parent[temp->nid] = start;
        temp = temp->next;
    }

    EDGELIST *mst = new_edgelist();
    while (h->size > 0) {
        hn = heap_extract_min(h); 
        int i = hn.value;
        if (T[i]==1){
            continue;
        }

        T[i] = 1; 
        insert_edge_end(mst, parent[i], i, hn.key); 
        temp = g->nodes[i]->neighbor;

        while (temp != NULL) {
            int neighbor_id = temp->nid;

            if (T[neighbor_id]==0){
                heapindex = heap_search_value(h, neighbor_id);

                if (heapindex >= 0) {
                    if (temp->weight < h->hda[heapindex].key) {
                        heap_change_key(h, heapindex, temp->weight);
                        parent[neighbor_id] = i;
                    }
                }
            
                else {
                    HEAPDATA new_hn;
                    new_hn.key = temp->weight;
                    new_hn.value = temp->nid;
                    heap_insert(h, new_hn);
                    parent[neighbor_id] = i;
                }
            }
            temp = temp->next;
        }
    }
    heap_clean(&h);
    return mst;
}

EDGELIST *spt_dijkstra(GRAPH *g, int start) {
    if (g==NULL) return NULL;
    EDGELIST *spt = new_edgelist();
    int i, heapindex, u, n = g->order;
    int T[n], parent[n], label[n];

    for (i = 0; i < n; i++) { 
        T[i] = 0; 
        parent[i] = -1;
        label[i] = INFINITY; 
    }
    HEAP *h = new_heap(4);
    label[start] = 0;
    T[start] = 1;
    ADJNODE *temp = g->nodes[start]->neighbor;
    HEAPDATA hn;

    while (temp != NULL){
        hn.key = label[start] + temp->weight;
        hn.value = temp->nid;
        heap_insert (h, hn);
        parent[temp->nid] = start;
        temp = temp->next;
    }

    while (h->size >0){
        hn = heap_extract_min(h);
        u = hn.value;

        if (T[u] == 1){
            continue;
        }

        T[u] = 1;
        label[u] = hn.key;
        insert_edge_end (spt, parent[u], u, label[u] - label[parent[u]]);

        temp = g->nodes[u]->neighbor;
        while (temp != NULL){
            int s = temp->nid;
            if (T[s] == 0){
                int distance = label[u] + temp->weight;
                heapindex = heap_search_value (h, s);
                if (heapindex >=0){
                    if (distance < h->hda[heapindex].key){
                        heap_change_key (h, heapindex, distance);
                        parent[s] = u;
                    }
                }
                else{
                    HEAPDATA new_hn;
                    new_hn.key = distance;
                    new_hn.value = s;
                    heap_insert (h, new_hn);
                    parent[s] = u;
                }
            }
            temp = temp->next;
        }
    }
    heap_clean(&h);
    return spt;
}

EDGELIST *sp_dijkstra(GRAPH *g, int start, int end) {
    if (g == NULL || start < 0 || start >= g->order || end < 0 || end >= g->order)
    {
        return NULL;
    }

    int n = g->order, heapindex, u;
    int T[n], parent[n], label[n];

    for (int i = 0; i < n; i++){
        T[i] = 0;
        parent[i] = -1;
        label[i] = INFINITY;
    }

    HEAPDATA hn;
    HEAP *h = new_heap(n);
    label[start] = 0;
    T[start] = 1;
    ADJNODE *temp = g->nodes[start]->neighbor;

    while (temp != NULL) {
        hn.key = temp->weight;
        hn.value = temp->nid;
        heap_insert(h, hn);
        parent[temp->nid] = start;
        temp = temp->next;
    }

    while (h->size > 0){
        HEAPDATA hn = heap_extract_min(h);
        u = hn.value;

        if (T[u] == 1){
            continue;
        }

        T[u] = 1;
        label[u] = hn.key;

        if (u == end){
            break;
        }

        temp = g->nodes[u]->neighbor;
        while (temp != NULL){
            int s = temp->nid;
            if (T[s] == 0) {
                int distance = label[u] + temp->weight;
                heapindex = heap_search_value(h, s);

                if (heapindex >= 0){
                    if (distance < h->hda[heapindex].key){
                        heap_change_key(h, heapindex, distance);
                        parent[s] = u;
                    }
                }
                else{
                    HEAPDATA new_hn;
                    new_hn.key = distance;
                    new_hn.value = s;
                    heap_insert(h, new_hn);
                    parent[s] = u;
                }
            }
            temp = temp->next;
        }
    }

    EDGELIST *sp = new_edgelist();
    int i = end;

    while (1){
        if (i == start){
            break;
        }
        insert_edge_start(sp, parent[i], i, label[i] - label[parent[i]]);
        i = parent[i];
    }

    heap_clean(&h);
    return sp;
}
