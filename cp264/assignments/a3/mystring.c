/**
* -------------------------------------
* @file mystring.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-01-31)}
*
* -------------------------------------
*/
#include "mystring.h"

/**
 * Count the number words of given simple string. A word starts with an English charactor end with a charactor of space, tab, comma, or period.  
 *
 * @param s - char pointer to a string
 * @return - return the number of words. 
 */
int str_words(char *s){
    if (s==0){
        return -1;
    }
    int count = 0;
    int start = 0;

    while (*s != '\0'){
        if (start == 0){
            if (((*s >='A' && *s<='Z') || (*s>='a' && *s<='z'))){
            count++;
            start=1;
            }
        }

        else if (*s ==' '|| *s==',' || *s=='.'){
            start =0;
        }
        s++;
    }
    return count;
}

/**
 * Change every upper case English letter to its lower case of string passed by s
 *
 * @param s - char pointer to a string
 * @return - return the number of actual flips.   
 */
int str_lower(char *s){
    if(s==0){
        return 0;
    }
    int index = 0;
    int flips = 0;

    while (*s != '\0'){
        if (*s >='A' && *s<='Z'){
            *s = 'a' + (*s- 'A');
            flips++;
        }
        index++;
        s++;
    }
    return flips;
}

/**
 * Remove unnecessary space characters in a simple string passed by `s`
 *
 * @param s - char pointer to a string
 */
void str_trim(char *s){
    char *p = s, *dp =s;
    while (*p){
        if (*p!=' ' || (p>s && *(p-1)!=' ')){
            *dp = *p;
            dp++;
        }
        p++;
    }

    if (*(p-1)!= ' '){
        *dp = '\n';
    }
    else{
        *(dp-1) = '\0';
    }
}