/**
* -------------------------------------
* @file matrix.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-01-23)}
*
* -------------------------------------
*/
#include <math.h>
#include "matrix.h"

float norm(float *v, int n) {
    float sum = 0;
    for (int x = 0; x<n;x++){
        sum += pow(v[x],2);
    }
    return sqrt(sum);
}

float dot_product(float *v1, float *v2, int n) {
    float sum = 0;

    for (int x = 0; x<n; x++){
        sum += v1[x] * v2[x];
    }
    return sum;
}

void matrix_multiply_vector(float *m, float *v, float *vout, int n) {
    int rowResult = 0;
    int count = 0;
    for (int x = 0;x<n;x++){
       for (int y = 0; y<n;y++){
           rowResult += (m[count]*v[x]);
           count++;
       }
       vout[x] = rowResult;
       rowResult = 0;
    }
}

void matrix_multiply_matrix(float *m1, float *m2, float *m3, int n) {
    int result = 0;
    int count=0;
    int row = 0;
    int col = 0;
    for (int x = 0;x<n;x++){
        for (int y = 0;y<n;y++){
            for (int s = 0;s<n;s++){
                result += m1[s+row] * m2[col + (s*n)];
            }
            m3[count] = result;
            result = 0;
            col++;
            if (col%n ==0){
                col = 0;
            }   
            count++;
        }
        row+=n;
   }
}
 