/**
* -------------------------------------
* @file avl.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-03-13)}
*
* -------------------------------------
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "avl.h"


AVLNODE *avl_node(RECORD data)
{
  AVLNODE *np = (AVLNODE *)malloc(sizeof(AVLNODE));
  if (np)
  {
    np->data = data;
    np->height = 1;
    np->left = NULL;
    np->right = NULL;
  }
  return np;
}


int max(int a, int b) 
{
  return (a > b)? a : b;
}


int height(AVLNODE *np)
{
    int height = 0;
    if (np != NULL){
        height = np->height;
    }
    return height;
}

int balance_factor(AVLNODE *np){
  if (np){
    return (height(np->left) - height(np->right));
  }
  else{
    return 0;
  }
    
}


AVLNODE *rotate_left(AVLNODE *np)
{
    AVLNODE *right = np->right;
    np->right = right->left;
    right->left = np;

    int leftHeight, rightHeight;
    //update np height
    leftHeight = height(np->left);
    rightHeight = height(np->right);
    np -> height = max(leftHeight, rightHeight) +1;

    //update right height
    leftHeight = height(right->left);
    rightHeight = height(right->right);
    right -> height = max(leftHeight, rightHeight) +1;

    return right;
}

AVLNODE *rotate_right(AVLNODE *root)
{
    AVLNODE *left = root->left;
    root->left = left->right;
    left->right = root;
    
    int leftHeight, rightHeight;
    //update np height
    leftHeight = height(root->left);
    rightHeight = height(root->right);
    root -> height = max(leftHeight, rightHeight) +1;

    //update left height
    leftHeight = height(left->left);
    rightHeight = height(left->right);
    left -> height = max(leftHeight, rightHeight) +1;

    return left;
}

AVLNODE *extract_smallest_node(AVLNODE **rootp) {
  AVLNODE *p = *rootp, *parent = NULL;
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

void avl_insert(AVLNODE **rootp, RECORD data)
{  
    // 1. Perform the normal BST insertion
    if (*rootp == NULL) {
        AVLNODE *np = (AVLNODE *) malloc(sizeof(AVLNODE));
        if (np) {
            np->data = data;
            np->height = 1;
            np->left = NULL;
            np->right = NULL;
        }
        *rootp = np;
    } 
    else {

        AVLNODE *root = *rootp;

        if (strcmp(data.name, root->data.name) == 0 )
            return;
        else if (strcmp(data.name, root->data.name) < 0 ) {
            avl_insert(&root->left, data);
        }
        else {
            avl_insert(&root->right, data);
        }

        // 2. update height of this ancestor node
        int leftHeight, rightHeight;
        leftHeight = height(root->left);
        rightHeight = height(root->right);
        root->height = max(leftHeight, rightHeight) +1;

        // 3. Get the balance factor of this ancestor node to check whether this node became unbalanced
        int balance = balance_factor (root);

        // 4. rebalance if not balanced
        if (balance>1){
            if (root->left != NULL && balance_factor(root->left)<0){
                root->left = rotate_left (root->left);
                root = rotate_right (root);
            }
            else{
                root = rotate_right(root);
            }
            
        }
        else if (balance <-1){
            if (root->right != NULL && balance_factor(root->right)>0){
                root ->right = rotate_right(root->right);
                root = rotate_left(root);
            }
            else{
                root = rotate_left(root);
            }
            
        }
        *rootp = root;
    }
    return;
}

void avl_delete(AVLNODE **rootp, char *name){
  AVLNODE *root = *rootp;
  AVLNODE *np;

  if (root == NULL) return;

  if (strcmp(name, root->data.name) == 0) {
    if (root->left == NULL && root->right == NULL) {
      free(root);
      *rootp = NULL;
    } else if (root->left != NULL && root->right == NULL) {
      np = root->left;
      free(root);
      *rootp = np;
    } else if (root->left == NULL && root->right != NULL) {
      np = root->right;
      free(root);
      *rootp = np;
    } else if (root->left != NULL && root->right != NULL) {
      np = extract_smallest_node(&root->right);
      np->left = root->left;
      np->right = root->right;
      free(root);
      *rootp = np;
    }
  } else {
    if (strcmp(name, root->data.name) < 0) {
      avl_delete(&root->left, name);
    } else {
      avl_delete(&root->right, name);
    }
  }

  // If the tree had only one node then return
  if (*rootp == NULL) return;
  root = *rootp;

  // STEP 2: UPDATE HEIGHT OF THE CURRENT NODE
  int leftHeight, rightHeight;
  leftHeight = height(root->left);
  rightHeight = height(root->right);
  root->height = max(leftHeight, rightHeight) +1;

  // STEP 3: GET THE BALANCE FACTOR OF THIS NODE 
  int balance = balance_factor (root);

  // STEP 4: rebalance if not balanced
  if (balance>1){
      if (root->left != NULL && balance_factor(root->left)<0){
          root->left = rotate_left (root->left);
          *rootp = rotate_right (root);
      }
      else{
          *rootp = rotate_right(root);
      }
      
  }
  else if (balance <-1){
      if (root->right != NULL && balance_factor(root->right)>0){
          root ->right = rotate_right(root->right);
          *rootp = rotate_left(root);
      }
      else{
          *rootp = rotate_left(root);
      }
      
  }

}

AVLNODE *avl_search(AVLNODE *root, char *name) {
    int comparison;
    while (root != NULL){
        comparison = strcmp(root->data.name, name);
        if (comparison == 0){
            return root;
        }
        else if (comparison <0){
            root = root->right;
        }
        else{
            root = root->left;
        }
    }

    return NULL;
}


void avl_clean(AVLNODE **rootp) {
  AVLNODE *root = *rootp;
  if (root) {
    if (root->left)
      avl_clean(&root->left);
    if (root->right)
      avl_clean(&root->right);
    free(root);
  }
  *rootp = NULL;
}