/**
* -------------------------------------
* @file myrecord_bst.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-03-07)}
*
* -------------------------------------
*/

#include <stdio.h>
#include <math.h>
#include "bst.h"
#include "myrecord_bst.h"

void add_record(BSTDS *ds, RECORD record) {
    if (bst_search(ds->root, record.name) == NULL){
        bst_insert(&(ds->root), record);
        float n = ds->count;
        ds->count+=1;
        float newmean = ((ds->mean * (ds->count-1)) + record.score)/ ds->count;
        float sd = sqrtf(((float)1/(n+1))*(n*((ds->stddev*ds->stddev)+(ds->mean*ds->mean))+(record.score*record.score))-(newmean*newmean));
        ds->mean = newmean;
        ds->stddev = sd;
    }
    return;
}

void remove_record(BSTDS *ds, char *name) {
    BSTNODE *node = bst_search (ds->root, name);
    if (node!=NULL){
        bst_delete (&(ds->root), name);
        float n = ds->count;
        ds->count -=1;
        if (ds->count == 0){
            ds->mean = 0.0;
            ds->stddev = 0.0; 
            return;
        }
        float newmean = ((ds->mean*(ds->count+1))- node->data.score)/ds->count;
        float sd = sqrtf(((float)1/(n-1))*(n*((ds->stddev*ds->stddev)+(ds->mean*ds->mean))-(node->data.score*node->data.score))-(newmean*newmean));
        ds->mean = newmean;
        ds->stddev = sd;
    }
    return;
}

void bstds_clean(BSTDS *ds) {
  bst_clean(&ds->root);
  ds->count = 0;
  ds->mean = 0;
  ds->stddev = 0;
}