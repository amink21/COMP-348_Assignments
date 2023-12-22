/*
* COMP-348 Assignment 1
*
* Author: Amin Kadawala - 40200998
*
* Replace file which contains the welcome message and main function.
*/
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <dirent.h>
#include <unistd.h>
#include "traversal.h"

/*
* Main function
*/
int main(int argc, char *argv[]){

    //If command line has 2 words, example (./a.out apple), it will proceed, if not then give error
    if (argc == 2){

        char *word = malloc(strlen(argv[1]));
        //copies the users word into variable word
        strcpy(word, argv[1]);
        
        //prints out welcome message for user, target word, and current folder.
        char currDir[100];
        printf("=========== COMP-348: Assignment 1 ===========\n");
        printf("Target Word: %s\n", word);
        printf("Search begins in current folder: %s\n\n", getcwd(currDir, sizeof(currDir))); 

        //call traversal to traverse the directory
        printf("** Search Report **\n\nUpdates    File Name\n");
        traversal(".", word);

        return 0;
    }

    //if user inputs something else
    else{
        printf("Error has occured, please try again. Thanks :)\n");
        return 1;
    }
}//ends