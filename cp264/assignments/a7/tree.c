/**
* -------------------------------------
* @file tree.c
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
#include "queue_stack.h"
#include "tree.h"

static int tree_height (TNODE *node){
    if (node == NULL){
        return 0;
    }

    int leftHeight = tree_height (node->left);
    int rightHeight = tree_height (node->right);

    if (leftHeight>=rightHeight){
        return leftHeight +1;
    }
    else{
        return rightHeight +1;
    }
}

static int node_count (TNODE *node){
    if (node == NULL){
        return 0;
    }

    return 1 + node_count(node->right) + node_count(node->left);
}

TPROPS tree_property(TNODE *root) {
    int height = tree_height(root);
    int count = node_count (root);

    TPROPS data = {count, height};
    return data;
}

void preorder(TNODE *root) {
    if (root != NULL){
        printf("%c ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
    return;
}

void inorder(TNODE *root) {
    if (root != NULL){
        inorder(root->left);
        printf("%c ", root->data);
        inorder(root->right);
    }
    return;
}

void postorder(TNODE *root) {
    if (root != NULL){
        postorder(root->left);
        postorder(root->right);
        printf("%c ", root->data);
    }
    return;
}

void bforder(TNODE *root) {
    if (root == NULL){
        return;
    }
    QUEUE q = {0};
    TNODE *current = NULL;
    enqueue (&q, root);
    while (q.front){
        current = dequeue(&q);
        if (current){
            printf("%c ", current->data);
            enqueue(&q, current->left);
            enqueue(&q, current->right);
        }
    }
}

TNODE *bfs(TNODE *root, char val) {
    TNODE *current = NULL, *p = NULL;
    if (root != NULL){
        QUEUE q = {0};
        enqueue (&q, root);
        while (q.front){
            p = dequeue(&q);
            if (p->data == val){
                current = p;
                break;
            }
            if (p->left) enqueue(&q, p->left);
            if (p->right) enqueue(&q, p->right);
        }

        clean_queue (&q);
    }
    return current;
}

TNODE *dfs(TNODE *root, char val) {
    TNODE *current = NULL, *p = NULL;
    if (root != NULL){
        STACK s = {0};
        push(&s, root);
        while (s.top){
            p = pop(&s);
            if (p -> data == val){
                current = p;
                break;
            }
            if (p->left) push(&s, p->left);
            if (p->right) push (&s, p->right);
        }
        
        clean_stack (&s);
    }

    return current;
}

TNODE *tree_node(char val) {
    TNODE *np = (TNODE *) malloc(sizeof(TNODE));
    if (np != NULL) {
        np->data = val;
        np->left = NULL;
        np->right = NULL;
    }
    return np;
}

void clean_tree(TNODE **rootp) {
    TNODE *p = *rootp;
    if (p) {
        if (p->left)
            clean_tree(&p->left);
        if (p->right)
            clean_tree(&p->right);
        free(p);
    }
    *rootp = NULL;
}

void insert_tree(TNODE **rootp, char val) {
    if (*rootp == NULL) {
        *rootp = tree_node(val);
    } else {
        QUEUE queue = { 0 };
        TNODE *p;
        enqueue(&queue, *rootp);
        while (queue.front) {
            p = dequeue(&queue);
            if (p->left == NULL) {
                p->left = tree_node(val);
                break;
            } else {
                enqueue(&queue, p->left);
            }

            if (p->right == NULL) {
                p->right = tree_node(val);
                break;
            } else {
                enqueue(&queue, p->right);
            }
        }
    }
}