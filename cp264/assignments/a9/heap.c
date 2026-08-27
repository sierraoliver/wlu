/**
* -------------------------------------
* @file heap.c
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
#include "heap.h"

int cmp(KEYTYPE a, KEYTYPE b) {
  int r = 0;
  if (a < b) r = -1;
  else if (a > b) r = 1;
  return r;
}

HEAP *new_heap(int capacity){
  HEAP *hp = (HEAP*) malloc(sizeof(HEAP));
  if (hp == NULL) return NULL;
  hp->hda = (HEAPDATA *) malloc(sizeof(HEAPDATA) * capacity);
  if ( hp->hda == NULL) { free(hp); return NULL; };
  hp->capacity = capacity;
  hp->size = 0;
  return hp;
}

// you may add this function to be used other functions.
int heapify_up(HEAPDATA *hda, int index) {
    int done = 0;
    while (done == 0){
        if (cmp(hda[index].key,hda[(index-1)/2].key)<0){
            HEAPDATA temp = hda[index];
            hda[index] = hda[(index-1)/2];
            hda[(index-1)/2] = temp;
            index = (index-1)/2;
        }
        else{
            done = 1;
        }
    }
    return index;
}

// you may add this function to be used other functions.
int heapify_down(HEAPDATA *hda, int n, int index) {
    int done = 0;
    while (done == 0){  
        if (index*2+1 < n || index*2+2 < n){
            if (cmp(hda[index].key,hda[(index*2)+1].key)>0 || cmp(hda[index].key, hda[(index*2)+2].key)>0){
                if (cmp(hda[(index*2)+1].key,hda[(index*2)+2].key)<=0){
                    HEAPDATA temp = hda[index];
                    hda[index] = hda[(index*2)+1];
                    hda[(index*2)+1] = temp;
                    index = (index*2) +1;
                }
                else{
                    HEAPDATA temp = hda[index];
                    hda [index] = hda[(index*2)+2];
                    hda[(index*2)+2] = temp;
                    index = (index*2)+2;
                }

            }
            else{
                done = 1;
            }
        }
        else{
            done = 1;
        }
        
    }
    return index;
}

void heap_insert(HEAP *heap, HEAPDATA new_node){
    heap->hda[heap->size] = new_node;
    heap->size++;
    if (heap->size == heap->capacity){
        heap->capacity *=2;
        void *temp = realloc(heap->hda, sizeof(HEAPDATA) *heap->capacity);
        if (temp){
            heap->hda = temp;
        }
        else{
            temp = malloc (sizeof(HEAPDATA) * heap->capacity);
            if (temp){
                memcpy (temp, heap->hda, sizeof(HEAPDATA) * heap->size);
                free (heap->hda);
                heap->hda = temp;
            }
            else{
                printf("array resize failed\n");
            }
        }
        
    }
    heapify_up(heap->hda, heap->size-1);
    return;
}

HEAPDATA heap_find_min(HEAP *heap){
    int index = 0;
    HEAPDATA *p = heap->hda;
    HEAPDATA min_value = *p;
    while (p){
        if (cmp(p->key,min_value.key)<0){
            min_value = *p;
        }
        p++;
        index ++;
        if (index >= heap->size){
            break;
        }
    }
    return min_value;
}

HEAPDATA heap_extract_min(HEAP *heap){
    HEAPDATA value = heap_find_min (heap);
    int index = heap_search_value (heap, value.value);
    heap->size-=1;
    if (heap->size <= (heap->capacity)/4 && heap->capacity>4){
        heap->capacity/=2;
        void *temp = realloc(heap->hda, sizeof(HEAPDATA) *heap->capacity);
        if (temp){
            heap->hda = temp;
        }
        else{
            temp = malloc (sizeof(HEAPDATA) * heap->capacity);
            if (temp){
                memcpy (temp, heap->hda, sizeof(HEAPDATA) * heap->size);
                free (heap->hda);
                heap->hda = temp;
            }
            else{
                printf("array resize failed\n");
            }
        }
    }
    if (heap->size>0){
        heap->hda[index] = heap->hda[heap->size-1];
        heapify_down(heap->hda, heap->size, index);
    }

    return value;
}

int heap_change_key(HEAP *heap, int index, KEYTYPE new_key){
    int final_index;
    heap->hda[index].key = new_key;
    if (cmp(heap->hda[index].key,heap->hda[(index-1)/2].key)<0){
        final_index = heapify_up(heap->hda, index);
    }
    else if (cmp(heap->hda[index].value,heap->hda[index/2+1].value)>0 || cmp(heap->hda[index].value,heap->hda[index/2+2].value)>0){
        final_index = heapify_down(heap->hda, heap->size, index);
    }
    return final_index;
}

int heap_search_value(HEAP *heap, VALUETYPE data) {
    int final_index = -1;
    int index = 0;
    HEAPDATA *node = heap->hda;
    while (node){
        if (node->value == data){
            final_index = index;
            break;
        }
        index++;
        node++;
        if (index >=heap->size){
            break;
        }
    }

    return final_index;
}

static HEAPDATA heap_extract_value (HEAP *heap){
    HEAPDATA value = heap->hda[0];
    heap->size-=1;
    if (heap->size <= (heap->capacity)/4 && heap->capacity>4){
        heap->capacity/=2;
        void *temp = realloc(heap->hda, sizeof(HEAPDATA) *heap->capacity);
        if (temp){
            heap->hda = temp;
        }
        else{
            temp = malloc (sizeof(HEAPDATA) * heap->capacity);
            if (temp){
                memcpy (temp, heap->hda, sizeof(HEAPDATA) * heap->size);
                free (heap->hda);
                heap->hda = temp;
            }
            else{
                printf("array resize failed\n");
            }
        }
    }
    if (heap->size>0){
        heap->hda[0] = heap->hda[heap->size-1];
        heapify_down(heap->hda, heap->size, 0);
    }

    return value;
}

static void heapify (HEAPDATA *heap, int n, int i){
    int largest = i;

    int left = 2*i +1;
    int right = 2*i +2;

    if (left<n && cmp(heap[left].value,heap[largest].value)>0){
        largest = left;
    }

    if (right<n && cmp(heap[right].value, heap[largest].value)>0){
        largest = right;
    }

    if (largest != i) {
        HEAPDATA temp = heap[i];
        heap[i] = heap[largest];
        heap[largest] = temp;
        heapify(heap,n,largest);
    }
    
}

void heap_sort(HEAPDATA *arr, int n){
    for (int x = (n/2)-1;x>=0;x--){
        heapify(arr,n,x);
    }
    
    for (int x = n-1; x>0;x--){
        HEAPDATA temp = arr[0];
        arr[0] = arr[x];
        arr[x] = temp;
        heapify(arr,x,0);
    }
        
}

void heap_clean(HEAP **heapp) {
  if (heapp) {
    HEAP *heap = *heapp;
    if (heap->capacity > 0) {
      heap->capacity = 0;
      heap->size = 0;
      free(heap->hda);
      free(heap);
    }
    *heapp = NULL;
  }
}