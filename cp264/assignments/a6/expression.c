/**
* -------------------------------------
* @file expression.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-02-27)}
*
* -------------------------------------
*/
#include <stdio.h>
#include <stdlib.h>
#include "common.h"
#include "queue.h"
#include "stack.h"
#include "expression.h"

QUEUE infix_to_postfix(char *infixstr) {
    char *p = infixstr;
    QUEUE queue = {0};
    STACK stack = {0};
    int sign = 1;
    int num = 0;

    while (*p){
        if (*p == '-' && (p == infixstr || *(p-1) == '(')){
            sign = -1;
        }
        else if (mytype(*p) == 0){
            num = *p -'0';
            while ((*(p+1) >= '0' && *(p+1) <= '9')) { 
                num = num*10 + *(p+1)-'0'; 
                p++; 
            }
            enqueue(&queue, new_node (sign*num, 0) );
            sign = 1;
        }
        else if (mytype(*p) == 1){
            push(&stack, new_node(*p,1));
            sign = 1;
        }
        else if (mytype(*p) == 2){ // equals '('
            push (&stack, new_node(*p,2));
            sign = 1;
        }
        else if (mytype(*p)==3){ // equals ')'         
            NODE *current = pop(&stack);
            while (current->data !='('){
                enqueue(&queue, current);
                current = pop(&stack);
            }
            sign = 1;
        }
        p++;
    }
    while (stack.top){
        enqueue(&queue, pop(&stack));
    }

    return queue;
}

int evaluate_postfix(QUEUE queue) {
    NODE *current = queue.front;
    STACK stack = {0};
    int type = 0;

    while (current){
        type = current->type;
        if (type == 0){
            push(&stack, new_node(current->data, 0));
        }
        else if (type == 1){
            int operator = current->data;
            NODE *operand2 = pop(&stack);
            if (operator == '+'){
                stack.top->data = stack.top->data + operand2->data;
            }
            else if (operator == '-'){
                stack.top->data = stack.top->data - operand2->data;
            }
            else if (operator == '*'){
                stack.top->data = stack.top->data * operand2->data;
            }
            else if (operator == '/'){
                stack.top->data = stack.top->data / operand2->data;
            }
            free (operand2);
        }
        current = current->next;
    }
    int result = stack.top->data;
    clean_stack (&stack);
    return result;

}

int evaluate_infix(char *infixstr) {
    QUEUE queue = infix_to_postfix(infixstr);
    int result = evaluate_postfix(queue);
    return result;
}
