/**
* -------------------------------------
* @file myrecord.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-02-06)}
*
* -------------------------------------
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include "myrecord.h"
#include "mysort.h"

GRADE grade(float score){
   GRADE r; 
   char g[14][5] = {"A+","A","A-","B+","B","B-","C+","C","C-","D+","D","D-","F"};
   int n[] = {100,90,85,80,77,73,70,67,63,60,57,53,50,0};
   int y = sizeof(n)/sizeof(float);
   int i = 0;
   for (i =0;i<y;i++){
    if (score>= n[i+1]){
        break;
    }
   }
   strcpy(r.letter_grade,g[i]);

   return r;   
}

int import_data(FILE *fp, RECORD *dataset) {
    char delimiters []= ",\n\r" ;
    char str [100];
    char *line = NULL;
    int record_counter = 0;
    while(fgets(str,sizeof(str),fp)!=NULL){
        line = (char*)strtok(str,delimiters);
        strcpy(dataset[record_counter].name,line);
        
        line = (char*)strtok(NULL, delimiters);
        sscanf(line, "%f", &dataset[record_counter].score);
        record_counter++;
    }
    
    return record_counter;
}

STATS process_data(RECORD *dataset, int count) { 
    STATS s; 
    float total = 0;
    float *numbers [count];  

    for (int x = 0;x<count;x++){
        total += dataset[x].score;
        numbers[x] = &dataset[x].score;
    }
    float mean = total/count;
    
    float sd = 0;
    total = 0;
    
    for (int y = 0;y<count;y++){
        total += pow(dataset[y].score - mean,2);
    }
    sd = sqrt(total/count);
    
    float median = 0;
    select_sort((void*)numbers, 0,count-1);
    
    if (count%2 == 0){
        median = (*(numbers[count/2-1])+*(numbers[count/2]))/2;
    }
    else{
        median = *(numbers[count/2]);
    }
    
    s.count = count;
    s.mean = mean;
    
    s.stddev= sd;
    s.median = median;
    
    return s;
}


int report_data(FILE *fp, RECORD *dataset, STATS stats) {
    int count = stats.count;

    if (count<1){
        return 0;
    }

    float *numbers [count];  
    for (int x = 0;x<count;x++){
        numbers[x] = &dataset[x].score;
    }
    select_sort((void*)numbers, 0, count-1);

    count-=1;
    while (count >=0){
        GRADE g = grade(dataset[count].score);
        int y = fprintf(fp,"%s:%.1f,%s\n", dataset[count].name,dataset[count].score,g.letter_grade);
        if (y == -1){
            return 0;
        }
        count--;
    }
    return 1;
}