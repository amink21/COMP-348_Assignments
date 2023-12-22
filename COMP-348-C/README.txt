What Works: 
- No hardcoded directory, just checks the current directory you are working on.
- Checking subdirectories and all txt files. 
- I have figured out the case insensitive, so if user inputs "apple", the text in the file of "Apple" or pineaPple would change to caps.
- I have used files, traversal.c, text.c, and replace.c with traversal and text having header files. No report.c file was made. 
- The report works, it outputs what we need as in the counter for the changes made in each file.

What does not work:
- No report.c file included, the report was conducted in the text.c file using a counter variable and whenever a word was found, it would be incremented.
- The report looks similar to the example in the assignment doc.
- The sorting of the report does not work (going from most changes to least), I have not implemented that.

//commands to what I was using, since no report.c, so not included.
gcc traversal.c text.c replace.c
./a.out string_word

Thank you and I appreciate the help. :)
Amin Kadawala - 40200998

