/**
* -------------------------------------
* @file bigint.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-02-14)}
*
* -------------------------------------
*/
#include <stdio.h>
#include <stdlib.h>
#include "bigint.h"

/* 
 * Creates and returns BIGINT object by converting the digit string.  
 */
BIGINT bigint(char *p) {
    BIGINT bn = {0};
    if (p == NULL) 
      return bn;
    else if (!(*p >= '0' && *p <= '9')) {// not begin with digits 
      return bn;
    }
    else if (*p == '0' && *(p+1) == '\0') {// just "0"
      dll_insert_end(&bn, dll_node(*p -'0'));
      return bn;
    }  
    else { 
      while (*p) {
        if (*p >= '0' && *p <= '9' ){
          dll_insert_end(&bn, dll_node(*p -'0'));
        } else {
          dll_clean(&bn);
          break;
        }
        p++;
      }
      return bn;
    }
  }

/* 
 * Add two BIGINT operants and returns the sum in BIGINT type.  
 * @param oprand1  - first operand of BIGINT type.
 * @param oprand2  - second operand of BIGINT type.
 * @return - the sum of oprand1 and oprand2 in BIGINT type.
 */
 BIGINT bigint_add(BIGINT oprand1, BIGINT oprand2){
    BIGINT sum = bigint(NULL);
    NODE* p1 = oprand1.end;
    NODE* p2 = oprand2.end;
    int c = 0, a, b, s;

    while (p1||p2){
      a = 0; 
      b = 0;

      if (p1){
        a = p1->data; 
        p1= p1->prev;
      }
      if (p2){
        b = p2->data;
        p2 = p2->prev;
      }
      s = a+b+c;
      if (s>=10){
        dll_insert_start (&sum, dll_node(s-10));
        c=1;
      }
      else{
        dll_insert_start(&sum, dll_node(s));
        c=0;
      }
    }

    if (c==1){
      dll_insert_start (&sum, dll_node(c));
    }

    return sum;

 }

 /* 
  * Compute and return Fibonacci(n) 
  * @param n - input positive integer
  * @return  - Fibonacci(n) in BIGINT type  
  */
 BIGINT bigint_fibonacci(int n){
    BIGINT f1 = bigint("0");
    BIGINT f2 = bigint("1");
    BIGINT temp = bigint(NULL);
    if (n==0){
      return f1;
    }
    else if (n==1){
      return f2;
    }

    for (int x = 1;x<n;x++){
      temp = bigint_add(f1,f2);
      f1 = f2;
      f2 = temp;
    }

    return temp;
 }