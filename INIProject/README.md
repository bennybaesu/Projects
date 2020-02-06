.INI PROJECT

AUTHOR: Benjamin Baesu

DATE: Feb 5, 2020

ABOUT:
This program is a command line program that takes in two arguments. The first is a path to a directory containing .ini files.
The second is a key word to be pair in each .ini file within the given directory. 

HOW TO CALL: In command line, get to proper directory that holds __main__.py. Enter: "python __main__.py <path> <description>

The program will end if:
- The incorrect number of arguments was passed in command line
- The path does not exist
- The path does not contain .ini files

If there are .ini files in the given directory, the program will print the name of the section and the keyed value.
For example, if the name of the section is [Student], and one of the key values is studentID=12345, and the description passed by the user is "studentID", the program will print "Student: 12345"

The program will not print any other key values other than the one specified by the user. 
