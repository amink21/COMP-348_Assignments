/*
* COMP-348 Assignment 1
*
* Author: Amin Kadawala - 40200998
*
* Text file where all the files are read and replaced.
*/
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include "text.h"

//defines constants
#define LINESIZE 5000
#define FILENAME 1000

/*
* This function reads the txt file and updates the file if word is found.
*
* @param filePath, the path for the txt file 
* @param wordPath, word pointer that the user inputted
*/
int read(char *filePath, char *wordPath){

    //creates file for the files in directory
    FILE *fp = fopen(filePath, "r");
    //temp file to store the text
    FILE *fTemp = fopen("temp.txt", "w");

    //char var for each line
    char *line = malloc(LINESIZE * sizeof(char));

    int count = 0;
    while (1){

        //if file ends
        if (feof(fp)){
            break;
        }

        //reads each line by one in file
        fgets(line, LINESIZE, fp);
        //count increments and checks if word is found
        count += wordFound(fTemp, line, wordPath);
    }

    //closes both files
    fclose(fp);
    fclose(fTemp);

    //removes file and replaces the temp with the normal file
    remove(filePath);
    rename("temp.txt", filePath);

    //prints out the counts for each file
    printf("%d%s%s\n", count, "          ", filePath);
    return 0;
}

/*
* This function occurs when a word is found using a lowercase word for case sensitive
* If word is found, it will call capitalize.
*
* @param fTemp, the file stream
* @param line, the full current line
* @param wordPath, the pointer for the word user inputted
*/
int wordFound(FILE *fTemp, char *line, char *wordPath){

    int i;
    //lowercase for char line
    char *lowerCaseLine = malloc((strlen(line) + 1) * sizeof(char) + 1);
    for (i = 0; line[i] != '\0'; i++){
        lowerCaseLine[i] = tolower(line[i]);
    }
    lowerCaseLine[i] = '\0';

    //lowercase for char word
    char *lowerCaseWord = malloc((strlen(wordPath) + 1) * sizeof(char) + 1);
    for (i = 0; wordPath[i] != '\0'; i++){
        lowerCaseWord[i] = tolower(wordPath[i]);
    }
    lowerCaseWord[i] = '\0';
    
    //strstr to see if the word is inside the line
    char *reference = strstr(lowerCaseLine, lowerCaseWord);

    int count = 0; //counter
    while (1){

        if (reference != NULL){

            //word found then call capitalize to capitalize the word
            capitalize(fTemp, line, wordPath, reference);
            count++; //increment counter for report
            
            //skips the lowercase version of word
            reference = reference + strlen(wordPath);
            //checks whether word is inside line
            reference = strstr(reference, wordPath);
        }

        else{
            break;
        }
    }

    fputs(line, fTemp); //puts the line in the temp file

    return count;
}

/*
* This function occurs when a word is found and needs capitalization.
* Capitalizes the word. 
*
* @param fTemp, the file stream
* @param line, the full current line
* @param wordPath, the pointer for the word user inputted
* @param reference, reference variable to keep in check
*/
void capitalize(FILE *fTemp, char *line, char *wordPath, char *reference){

    //for loop to capitalize each char one by one
    for (int i = 0; i < strlen(wordPath); i++){

        char replaceWord = toupper(line[strlen(line) - strlen(reference) + i]);
        //makes the lowercase uppercase
        line[strlen(line) - strlen(reference) + i] = replaceWord;
    }
} //ends