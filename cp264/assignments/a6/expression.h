/**
* -------------------------------------
* @file expression.h
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-02-27)}
*
* -------------------------------------
*/

#ifndef EXPRESSION_H
#define EXPRESSION_H

#include "common.h"
#include "queue.h"

/* 
 * Convert infix expression string to postfix expression reprsented by queue data structure. 
 * @param infixstr - string of infix expression. 
 * @return - postfix expression in queue of QUEUE type. 
*/
QUEUE infix_to_postfix(char *infixstr);

/* 
 * Evaluate and return the value postfix expression passed by queue.
 * @parame queue - postfix expression in queue of QUEUE type.
 ^ @return - value of postfix expression
*/
int evaluate_postfix(QUEUE queue);

/* 
 * Evaluate and return the value of infix expression passed by string infixstr, 
 * using infix_to_postfix() and evaluate_postfix() functions.
 * @param infixstr - string of infix expression.  
 * @return - value of the infix expression.
*/
int evaluate_infix(char *infixstr);

#endif