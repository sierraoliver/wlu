/**
* -------------------------------------
* @file file_directory.c
* file description
* -------------------------------------
* @author Sierra Oliver, 169067437, oliv7437@mylaurier.ca
*
* @version (date: 2025-05-25)
*
* -------------------------------------
*/
#define _XOPEN_SOURCE 500
#include <errno.h>
#include <dirent.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <ftw.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/*
* create a directory with given name and permissions
*/
void create_directory (const char *dir_name, mode_t mode){
    int result = mkdir(dir_name, mode); //create directory

    //if successful
    if (result == 0){
        printf("Directory %s created successfully\n", dir_name);
    }

    //otherwise, error
    else{
        printf("Error in creating directory %s\n", dir_name);
        printf("Error code: %d\n", errno);
    }

    return;
}

/*
* create a file with a given name and write text to the file
*/
void create_write_file (const char *file_name, const char *content){
    FILE *ptr;

    //try to open file
    ptr = fopen(file_name, "w");
    if (ptr == NULL){
        printf("Error opening file\n");
        return;
    }

    //write given content to file
    if (fprintf(ptr, "%s",content)<0){
        perror("Write error");
        fclose(ptr);
        return;
    }

    //close file
    fclose(ptr);

    printf("File created and written to successfully\n");

    return;
}

/*
* extract and save key information about a system's memory
* from /proc/meminfo to a file
*/
void read_proc_mem_info_to_file (const char *file_name){
    FILE *ptr;
    char line [100];

    //try to open file to read
    ptr = fopen("/proc/meminfo", "r");
    if (ptr == NULL){
        perror("Error opening /proc/meminfo");
        return;
    }

    FILE *write;

    //try to open file to write
    write = fopen(file_name, "w");
    if (write == NULL){
        printf("Error opening file for writing\n");
        return;
    }

    //read each line and then write to file
    while (fgets(line, sizeof(line), ptr) != NULL){
        if(fprintf(write, "%s", line)<0){
            perror("Write error");
            fclose(ptr);
            fclose(write);
            return;
        }
    }

    //close files
    fclose(ptr);
    fclose(write);

    printf("/proc/meminfo read and written to %s successfully\n", file_name);

    return;

}

/*
* recursively lists all files and subdirectores in a given
* directory and its subdirectories - print this list to standard output
*/
void directory_listing (const char *start_dir){
    static int depth = 0;
    DIR *dir;
    struct dirent *entry;

    //open directory
    dir = opendir(start_dir);
    if (dir == NULL){
        perror("Unable to open directory");
        return;
    }

    //loop through each entry in the directory
    while ((entry = readdir(dir))!= NULL){
        if (strcmp(entry->d_name, ".")!= 0 && strcmp(entry->d_name, "..")!=0){

            char full_path [4096];
            snprintf(full_path, sizeof(full_path), "%s/%s", start_dir, entry->d_name);

            //makes directories more obvious visually
            //essentially, to indicate subdirectories
            for (int x = 0; x<depth;x++){
                printf("  ");
            }
            if (depth>0){
                printf("└──");
            }
            else{
                printf("├──");
            }

            printf("%s\n", entry->d_name);
            
            struct stat filestat;
            //recursviely deletes subdirectories
            if (stat(full_path, &filestat) == 0 && S_ISDIR(filestat.st_mode)) {
                depth++;
                directory_listing(full_path);
                depth--;
            }
        }
    }

    //close directory
    closedir(dir);

    return;

}

int unlink_cb(const char *fpath, const struct stat *sb, int typeflag, struct FTW *ftwbuf) {
    int ret = remove(fpath); //try to delete file or directory

    //if deletion fails, print error
    if (ret !=0){
       perror(fpath); 
    }
        
    return ret;
}

/*
* removes a given directory and its subdirectories from the system
*/
void remove_directory (const char *dir_name){
    char c;

    //gives user warning
    printf("Warning: you are about to delete the directory %s and all of its contents recursively.\n", dir_name);
    printf("Proceed? (y/n): ");
    scanf(" %c", &c); 

    //check if user entered no
    if (c == 'n' || c == 'N') {
        printf("Operation cancelled.\n");
        return;
    } 
    
    //check if user entered yes
    else if (c == 'y' || c == 'Y') {
        //walk through files and delete them
        if (nftw(dir_name, unlink_cb, 64, FTW_DEPTH | FTW_PHYS) == 0) {
            printf("Directory '%s' and its contents deleted successfully.\n", dir_name);
        } 
        
        else {
            perror("Error deleting directory");
        }
    } 
    
    //if neither y/n are input, print error
    else {
        printf("Invalid input. Operation cancelled.\n");
	while (getchar()!= '\n'); // clear input 
    }

    return;
}

int main(){
    int choice;
    char dir_name[256];
    char file_name[256];
    char content[] = "Operating systems is Fun !!!"; 

    while (1) {
        //print operation menu for user to see and select options
        printf("File & Directory Operations Menu\n");
        printf("1. Create directory\n");
        printf("2. Create and write to file\n");
        printf("3. Read /proc/meminfo and save to file\n");
        printf("4. List directory contents\n");
        printf("5. Remove directory\n");
        printf("99. Exit\n");
        printf("Enter your choice: ");
        
        if (scanf("%d", &choice) != 1) {
            printf("Invalid input. Please enter a number.\n");
            while (getchar() != '\n');
            continue;
        }

        //get correct input information and call correct function
        //based on input from user
        switch (choice) {
            case 1:
                printf("Enter directory name: ");
                scanf("%s", dir_name);
                create_directory(dir_name, 0755); 
                break;
            case 2:
                printf("Enter file name: ");
                scanf("%s", file_name);
                create_write_file(file_name, content);
                break;
            case 3:
                printf("Enter output file name: ");
                scanf("%s", file_name);
                read_proc_mem_info_to_file(file_name);
                break;
            case 4:
                printf("Enter directory to list: ");
                scanf("%s", dir_name);
                directory_listing(dir_name);
                break;
            case 5:
                printf("Enter directory to remove: ");
                scanf("%s", dir_name);
                remove_directory(dir_name);
                break;
            case 99:
                return 0;
            default:
                printf("Invalid option. Please choose a valid menu item.\n");
        }
    }

    return 0;
}