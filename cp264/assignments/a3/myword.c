/**
* -------------------------------------
* @file myword.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-01-31)}
*
* -------------------------------------
*/
#include <string.h>
#include <stdio.h>
#include "mystring.h"
#include "myword.h"

#define MAX_LINE_LEN 1000
#define MAX_WORDS 1000

/*
 * Load word data from file, and insert words a directory represented by char array.
 * 
 * @param  FILE *fp -   file pointer to an opened text file
 * @param *dictionary - char pointer to a char array where dictionary words are stored. 
 *                      It's up to your design on how to store words in the char array.
 * @return - the number of words added into the dictionary.   
 */
int create_dictionary(FILE *fp, char *dictionary) {
    char line[1000];
    char delimiters[] = ".,\n\t\r";
    int count = 0;
    char *token;
    while (fgets(line,1000,fp)!= NULL){
        str_lower(line);
        str_trim(line);
        token = (char*) strtok(line, delimiters);
        while(token!=NULL){
            count++;
            strcat(dictionary,token);
            strcat(dictionary,",");
            token=(char*)strtok(NULL,delimiters);
        }
    }
    return count;
}

/*
 * Determine if a given word is contained in the given dictionary.  
 * 
 * @param *dictionary -  char pointer to a char array of given dictionary.
 * @param *word  -  pointer to a given word.  
 *                     
 * @return - TRUE if the word is in the dictionary, FALSE otherwise.   
 */
BOOLEAN contain_word(char *dictionary, char *word) {
    char *line;
    if (word == NULL || *word == 0){
        return FALSE;
    }
    else{
        char temp [20] = {0};
        strcat(temp,",");
        strcat(temp,word);
        strcat(temp,",");
        line = (char*)strstr(dictionary,temp);
        if (line != NULL){
            return TRUE;
        }
        else{
            return FALSE;
        }
    }
}

/*
 * Process text data from a file for word statistic information of line count, word count, keyword count, and frequency of keyword.   
 * 
 * @param *fp -  FILE pointer of input text data file. .
 * @param *words  -  WORD array for keywords and their frequencies.
 * @param *dictionary  -  stop-word/common-word dictionary.    
 *                     
 * @return - WORDSTATS value of processed word stats information.   
 */
WORDSTATS process_words(FILE *fp, WORD *words, char *dictionary) {
    WORDSTATS ws = {0};
    char line[1000];
    char delimiters[] = " .,;:!()&?-\n\t\r\"\'";
    char *token;
    int j = 0;
    int found = 0;

    while (fgets(line,MAX_LINE_LEN,fp)!= 0){
        ws.line_count++;
        str_lower(line);
        str_trim(line);
        token = (char*) strtok(line, delimiters);
        while(token!=NULL){ 
            if (contain_word (dictionary, token)==FALSE){
                while(j<ws.keyword_count &&strcmp(token,words[j].word)!=0){
                    j++;
                }
                if (j<ws.keyword_count){
                    words[j].count++;
                }   
                else{
                    strcpy(words[j].word,token);
                    words[j].count = 1;
                    ws.keyword_count++;
                }
                
            }
            ws.word_count++;
            token=(char*)strtok(NULL,delimiters);
        }
    }
    return ws;
}
