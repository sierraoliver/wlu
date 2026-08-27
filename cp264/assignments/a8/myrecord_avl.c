/**
* -------------------------------------
* @file myrecord_avl.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-03-14)}
*
* -------------------------------------
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "avl.h"
#include "myrecord_avl.h"

void avl_merge(AVLNODE **dest_rootp, AVLNODE **source_rootp){
    if (*source_rootp == NULL){
        return;
    }
    if (avl_search(*dest_rootp,(*source_rootp)->data.name)!=NULL){
        avl_insert(dest_rootp,(*source_rootp)->data);
    }
    avl_merge(dest_rootp, &((*source_rootp)->left));
    avl_merge(dest_rootp, &((*source_rootp)->right));
}

void avlds_merge(AVLDS *dest, AVLDS *source){
    avl_merge (&dest->root, &source->root);

    float c1 = dest->count, c2 = source->count;
    float count = c1+c2;
    float m1 = dest->mean, m2 = source->mean;
    float mean = (m1 * c1 + m2 * c2)/count;
    float sd1 = dest->stddev;
    float sd2 = source->stddev;
    float stddev = sqrtf((1/count)*(sd1*sd1*c1+m1*m1*c1+sd2*sd2*c2+m2*m2*c2)-(mean*mean));

    dest->count = (int)count;
    dest->mean = mean;
    dest->stddev = stddev;
    avlds_clean (source);
}


void avlds_clean(AVLDS *ds) {
    avl_clean(&ds->root);
    ds->count = 0;
    ds->mean = 0;
    ds->stddev = 0;
}

// the following functions are adapted from a7q3
void add_record(AVLDS *tree, RECORD data) {
  if (avl_search(tree->root, data.name) == NULL) {
    avl_insert(&(tree->root), data);
    int count = tree->count;
    float mean = tree->mean;
    float stddev = tree->stddev;
    tree->count = count + 1;
    tree->mean =  (mean*count + data.score) / (count+1.0);
    tree->stddev = sqrt(data.score*data.score/(count+1.0) + (stddev * stddev + mean * mean) * (count/(count+1.0)) - tree->mean * tree->mean );
  } else {
    printf("record exits");
  }
}

void remove_record(AVLDS *tree, char *name) {
  AVLNODE *np = NULL;
  if ( (np = avl_search(tree->root, name)) != NULL) {
    float score = np->data.score;
    avl_delete(&(tree->root), name);
    float count = tree->count;
    float mean = tree->mean;
    float stddev = tree->stddev;
    tree->count = count - 1;
    if (count >= 3) {
      tree->mean =  (mean*count - score) / (count-1.0);
      tree->stddev = sqrt( (stddev * stddev + mean * mean) * (count/(count-1.0)) - score*score/(count-1.0) - tree->mean * tree->mean );
    }
    else if (count == 2) {
        tree->mean = mean*count - score;
        tree->stddev = 0;
   }
   else {
        tree->mean = 0;
        tree->stddev = 0;
    }
  } else {
    printf("record does not exit");   
  }     
}