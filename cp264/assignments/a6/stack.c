/**
* -------------------------------------
* @file stack.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-02-27)}
*
* -------------------------------------
*/

#include <stdio.h>
#include "stack.h"

void push(STACK *sp, NODE *np) {
    np->next = sp->top;
    sp->top = np;
    sp->length+=1;
}

NODE *pop(STACK *sp) {
    NODE *remove = NULL;

    if (sp->length >0){
        remove = sp->top;
        sp->top = sp->top->next;
        sp->length-=1;
        remove->next = NULL;
    }
    
    return remove;
}

void clean_stack(STACK *sp) {
  clean(&(sp->top));
  sp->top = NULL;
  sp->length=0;
}