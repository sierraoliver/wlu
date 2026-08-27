/**
* -------------------------------------
* @file fibonacci.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-01-22)}
*
* -------------------------------------
*/
#include "fibonacci.h"

int recursive_fibonacci(int n) {
    if (n<=1){
        return n;
    }
    else{
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2);
    }
    
}

int iterative_fibonacci(int n)
{
    if (n==0 || n==1){
        return n;
    }
   int behindNumber = 0, previous = 1, current;

   for (int x = 1; x<n;x++) {
        current = behindNumber + previous;
        behindNumber = previous;
        previous = current;
   }
   return current;
}

int dpbu_fibonacci(int *f, int n) {
    f[0] = 0;
    if (n>=1){
        f[1] = 1;
    }
    for (int x = 2;x<=n;x++){
        f[x] = f[x-1] + f[x-2];
    }
    return f[n];
}

int dptd_fibonacci(int *f, int n) {
    if (n <=1){
        return n;
    }
    if (f[n] >0){
        return f[n];
    }
    else{
        f[n] = dptd_fibonacci(f, n-2) + dpbu_fibonacci(f, n-1);
        return f[n];
    }
}