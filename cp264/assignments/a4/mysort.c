/**
* -------------------------------------
* @file mysort.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-02-05)}
*
* -------------------------------------
*/
#include "mysort.h"
#include <stdio.h>

// swap pointers
void swap(void **x, void **y) {
     void *temp = *y;
     *y = *x;
     *x = temp;
}

// a compare floating values pointed by void pointers. 
int cmp(void *x, void *y) {
   float a = *(float*)x;
   float b = *(float*)y; 
     if (a > b) return 1;
     else if (a < b) return -1;
     else return 0;
}   

void select_sort(void *a[], int left, int right){
   while (left<=right){
        int min_index = left;
        for (int x = left;x<=right;x++){
            if (cmp(a[min_index],a[x])==1){
                min_index = x;
            }
        }
        swap(&a[left],&a[min_index]);
        left++;
   }

}

void quick_sort(void *a[], int left, int right){ 
    if (left<right){
        int i = left;
        int j = right-1;
        while (i<=j){
            while (i<right && cmp(a[i],a[right])==-1){
                i++;
            }
            while (j>=left && cmp(a[j],a[right])==1){
                j--;
              
            }
            if (i<j){
                swap(&a[i],&a[j]);
            }

            else{
                swap(&a[i],&a[right]);
            }
           
            quick_sort(a,i+1,right);
            quick_sort(a,left,i-1);
            break;
           
        } 
    }
   
}

void my_sort(void *a[], int left, int right, int (*cmp)(void*, void*) ){ 
    int comparison = 0;
    while (left<=right){
        int min_index = left;
        for (int x = left;x<=right;x++){
            comparison = (*cmp)((void*)a[min_index],(void*)a[x]);
            if (comparison==1){
                min_index = x;
            }
        }
        swap(&a[left],&a[min_index]);
        left++;
    }
}
