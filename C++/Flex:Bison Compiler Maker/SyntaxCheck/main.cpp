#include <stdio.h>
#include <string>
#include "program.tab.h"
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int yyerror(char const* s)
{
    fprintf(stderr, "%s\n", s);
    return 0;
}

void set_input_string(const char* in);
void end_lexical_scan(void);

int main()
{
   /* fstream _file;
    _file.open("CleanedCode.txt", ios::out | ios::in);
    stringstream code;

    if (_file.is_open())
    {
        code << _file.rdbuf();
        _file.flush();
    }*/

    string input = "PROGRAM aba13;"
        "VAR"
        "ab5, cb, be, eb: INTEGER;"
        "BEGIN"
        "ab5 = 5;"
        "cb = 10;"
        "PRINT('ab5', ab5);"
        "eb = cb + ab5;"
        "PRINT(eb);"
        "be = 2 * abc5 + eb;"
        "PRINT(be);"
        "END.";

    input.erase(remove_if(input.begin(), input.end(), isspace), input.end());
    set_input_string(input.c_str());
    yyparse();
    return 0;
}