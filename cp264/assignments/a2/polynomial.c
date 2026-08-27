/**
* -------------------------------------
* @file polynomial.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-01-22)}
*
* -------------------------------------
*/

#include <stdio.h>
#include "polynomial.h"
#define EPSILON 1e-6
#define MAXCOUNT 100

float horner(float *p, int n, float x)
{
    float result = 0;

    for (int y = 0; y<n;y++){
        result = result*x + p[y];
    }

    return result;
}

void derivative(float *p, float *d, int n)
{
    int counter = 0;
    for (int x = (n-1); x>=0 ;x--){
        d[counter] = p[counter] * x;
        counter++;
    }
}

float myfabs(float x){

    if (x <0){
        x *=-1;
    }
    return x;
}


float newton(float *p, int n, float x0)
{
    float d [n-1];
    derivative(p,d,n);
    int counter = 0;
    float currentx = x0;

    while (counter != MAXCOUNT){
        float derValue = horner(d,n-1,currentx);
        float eqValue = horner(p,n,currentx);
        if (myfabs(eqValue) < EPSILON){
            return currentx;
        }
        else if (derValue!= 0){   
            currentx = currentx - (eqValue/derValue);
        }
        else{
            return currentx;
        }
        counter++;
    }
    return x0;


}
