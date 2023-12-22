//header file for text
#ifndef TEXT_H_
#define TEXT_H_

int read(char *filePath, char *wordPath);
int wordFound(FILE *fTemp, char *line, char *wordPath);
void capitalize(FILE *fTemp, char *line, char *wordPath, char *reference);

#endif