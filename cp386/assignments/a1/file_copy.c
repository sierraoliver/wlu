/**
* -------------------------------------
* @file file_copy.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-05-26)
*
* -------------------------------------
*/

#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Insufficient parameters passed.\n");
        return 1; 
    }
    else{
        FILE *input;

        if (access(argv[1], R_OK) ==-1){
            perror("Read access denied");
            return 1;
        }

        input = fopen(argv[1], "r");
        if (input== NULL){
            perror("Error opening input file");
            return 1;
        }


        FILE *output;
        if (argc >=3){
            //check if file exists
            if (access(argv[2], F_OK) == 0) { 
                //if it does exist try to delete it
                if (unlink(argv[2]) == -1) {
                    perror("Failed to delete existing output file");
                    fclose(input);
                    return 1;
                }
            }

            //if file successfully deleted or file doesnt exist open it
            output = fopen(argv[2], "w");

        }
        else{
            //check if file exsits
            if (access("output.txt", F_OK) == 0) {
                //if it does exist try to delete it
                if (unlink("output.txt") == -1) {
                    perror("Failed to delete existing output file");
                    fclose(input);
                    return 1;
                }
            }

            //if file successfully deleted or file doesnt exist open it
            output = fopen("output.txt", "w");
        }

        if (output == NULL){
            perror("Error creating output file");
            return 1;
        }


        char line [100];

        //write lines from input file to output file
        while (fgets(line, sizeof(line), input) != NULL){ 
            if(fprintf(output, "%s", line)<0){ //check for write error
                perror("Write error");
                fclose(input);
                fclose(output);
                return 1;
            }
        }

        fclose(input);
        fclose(output);

        printf("The contents of file %s have been successfully copied into the %s file.\n", argv[1], argc >= 3 ? argv[2] : "output.txt");
    }

    return 0;
}