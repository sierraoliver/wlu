/**
* -------------------------------------
* @file bst.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-03-07)}
*
* -------------------------------------
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "bst.h"


BSTNODE *bst_search(BSTNODE *root, char *key) {
    while(root != NULL){
        int cmp = strcmp(root->data.name, key);
        if (cmp>0){
            root = root->left;
        }
        else if (cmp<0){
            root = root->right;
        }
        else {
            return root;
        }
    }
    return NULL;
}

void bst_insert(BSTNODE **rootp, RECORD data) {
    BSTNODE *new = bst_node (data);
    if (*rootp == NULL){
        *rootp = new;
        return;
    }

    BSTNODE *p = *rootp;
    while(1){
        int cmp = strcmp (data.name, p->data.name);
        if (cmp == 0){
            return;
        }
        else if (cmp<0){
            if (p->left == NULL){
                p->left = new;
                break;
            }
            else{
                p = p->left;
            }
        }
        else{
            if (p->right == NULL){
                p->right = new;
                break;
            }
            else{
                p = p->right;
            }
        }
    
    }
   
    return;
}

void bst_delete(BSTNODE **rootp, char *key) {
    if (*rootp == NULL){
        return;
    }
    BSTNODE *previous = NULL;
    BSTNODE *p = *rootp, *temp;
    while(1){
        int cmp = strcmp (key, p->data.name);
        if (cmp == 0){
            if (p->right == NULL && p->left == NULL){
                if (previous == NULL){
                    *rootp = NULL;
                }
                else if (previous->right == p){
                    previous->right = NULL;
                }
                else{
                    previous->left = NULL;
                }
                free(p);
            }
            else if (p->right == NULL){
                if (previous == NULL){
                    *rootp = p->left;
                }
                else if (previous->right == p){
                    previous->right = p->left;
                }
                else{
                    previous->left = p->left;
                }
                free(p);
            }
            else if (p->left == NULL){
                if (previous == NULL){
                    *rootp = p->right;
                }
                else if (previous->right == p){
                    previous->right = p->right;
                }
                else{
                    previous->left = p->right;
                }
                free (p);
            }
            else{
                temp = extract_smallest_node (&p->right);
                temp ->left = p->left;
                temp->right = p->right;
                previous = temp;
                free (p);
            }
            break;
        }
        else if (cmp<0){
            previous = p;
            p = p->left;
        }
        else{
            previous = p;
            p = p->right;
        }
    
    }
}


BSTNODE *bst_node(RECORD data) {
    BSTNODE *np = (BSTNODE *) malloc(sizeof(BSTNODE));
    if (np) {
        memcpy(np, &data, sizeof(BSTNODE));
        np->left = NULL;
        np->right = NULL;
    }
    return np;
}

void bst_clean(BSTNODE **rootp) {
    BSTNODE *root = *rootp;
    if (root) {
        if (root->left)
            bst_clean(&root->left);
        if (root->right)
            bst_clean(&root->right);
        free(root);
    }
    *rootp = NULL;
}

BSTNODE *extract_smallest_node(BSTNODE **rootp) {
    BSTNODE *p = *rootp, *parent = NULL;
    if (p) {
        while (p->left) {
            parent = p;
            p = p->left;
        }

        if (parent == NULL)
            *rootp = p->right;
        else
            parent->left = p->right;

        p->left = NULL;
        p->right = NULL;
    }

    return p;
}
