/*
* COMP-348 Assignment 1
*
* Author: Amin Kadawala - 40200998
*
* Traversal file where the traversal occurs of all directories and files.
*/
#include <stdio.h>
#include <dirent.h>
#include <string.h>
#include <stdlib.h>
#include "text.h"

//defines constants
#define LINESIZE 5000
#define FILENAME 1000

/*
* This function opens the directory by the user and traverses it, opening the subdirectories
* and files. Determins whether it is a file or directory.
*
* @param dir, directory name
* @param word, word the user wants to capitalize in all files
*/
int traversal(char *dir, char *word){

    DIR *d;
    struct dirent *entry;
    d = opendir(dir);

    //if directory is null
    if (d == NULL){
        printf("Error. Directory is null. Please try again.\n");
        return 1;
    }

    //goes through directory
    while ((entry = readdir(d)) != NULL){

        //will continue if directory is . or ..
        if (!strcmp(entry->d_name, ".") || !strcmp(entry->d_name, "..")){
            continue;
        }
        
        //to determine whether its a directory
        if (entry->d_type == DT_DIR){

            char directory[FILENAME] = "";
            strcpy(directory, dir);
            strcat(directory, "/");
            strcat(directory, entry->d_name);

            //recursive, so the directory will check again whether it is directory or file
            traversal(directory, word);
            continue;
        }

        //to determine whether its a txt file
        if (strstr(entry->d_name, ".txt") != NULL){
            
            char txtFile[FILENAME] = "";
            strcpy(txtFile, dir);
            strcat(txtFile, "/");
            strcat(txtFile, entry->d_name);

            char *filePath = txtFile;

            //calls read which reads the file and updates each word to capitalize
            read(filePath, word);

        }
    }
    return 0;
} //end