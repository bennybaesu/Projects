//%define api.value.type{ char const* }
%{
#include <stdio.h>
#include <string>
#include "program.tab.h"
#include <iostream>
#include <fstream>
#include <sstream>
#define YYDEBUG 1
using namespace std;
int yylex();
int yyerror(char const *s);
stringstream code;
%}

%token digit abcdef str PROGRAM SEMICOLON VAR INTEGER COLON COMMA BEGINCOPY CLOSEPAR OPENPAR PRINT MULTIPLY DEVIDE ADD SUBTRACT EQUAL END DOT;

%type<c> Assign Print Stat Start Number Letter Id digit 
abcdef str Colon PROGRAM Program Comma SEMICOLON Var Dec-list 
Dec Begin Semicolon Stat-list Dot End VAR INTEGER Integer 
COLON COMMA BEGINCOPY CLOSEPAR OPENPAR PRINT MULTIPLY DEVIDE Str
ADD SUBTRACT EQUAL END DOT OpenPar ClosePar Output Expr Term Factor Equal

%union{
    char* c;
}

%%
Start: Program Id Semicolon Var Dec-list Colon Integer Semicolon Begin Stat-list End Dot;

Dec-list: Dec;

Dec: Id Comma Dec { code << "int" << " " << $$ << ";" << endl; }
| Id { code << "int" << " " << $$ << ";" << endl; };

Stat-list: 
Stat Semicolon
| Stat Semicolon Stat-list;

Stat: 
Print
| Assign;

Print: PRINT OpenPar Output ClosePar

Output: 
Str Comma Id { code << "cout" << " << " << $1 << " << " << $3 << ";" << endl; };
| Id { code << "cout" << " << " << $1 << ";" << endl; };

Assign: Id Equal Expr { code << $1 << $2 << $3 << ";" << endl; };

Expr: 
Term ADD Expr { strcat($$, $2); strcat($$, $3); }
| Term SUBTRACT Expr { strcat($$, $2); strcat($$, $3); }
| Term;

Term: 
Factor MULTIPLY Term { strcat($$, $2); strcat($$, $3); }
| Factor DEVIDE Term { strcat($$, $2); strcat($$, $3); }
| Factor;

Factor: 
Id
| digit 
| OpenPar Expr ClosePar;


Id: 
Letter { $$ = $1; }
| Letter Number { strcat($$, $1); strcat($$, $2); };

Letter: 
abcdef 
| abcdef Number { strcat($$, $2); };

Number: 
digit
| digit Letter { strcat($$, $2); };



Equal: EQUAL | error { printf("= is missing\n"); YYABORT;};
Colon: COLON | error { printf(": is missing\n"); YYABORT; } ;
OpenPar: OPENPAR | error { printf("( is missing\n"); YYABORT;};
ClosePar: CLOSEPAR | error { printf(") is missing\n"); YYABORT;};
Comma: COMMA | error { printf(", is missing\n"); YYABORT;};
Semicolon: SEMICOLON | error { printf("; is missing\n"); YYABORT;};
Dot: DOT | error { printf(". is missing\n"); YYABORT;};
Str: str | error{ printf("\" is missing\n"); YYABORT; };

Var: VAR | error { printf("VAR is expected\n"); YYABORT;};
Begin: BEGINCOPY | error { printf("BEGIN is expected \n"); YYABORT;};
Integer: INTEGER | error { printf("INTEGER is expected\n"); YYABORT;};
Program: PROGRAM | error { printf("PROGRAM is expected\n"); YYABORT;};
End: END | error { printf("END is expected\n"); YYABORT;};


%%





int yyerror(char const* s)
{
    fprintf(stderr, "%s\n", s);
    return 0;
}

void set_input_string(const char* in);
void end_lexical_scan(void);

int main()
{
     fstream _CleanedCode;
     _CleanedCode.open("CleanedCode.txt", ios::in);
     stringstream cleanedCode;

     if (_CleanedCode.is_open())
     {
         cleanedCode << _CleanedCode.rdbuf();
         _CleanedCode.flush();
     }

     fstream _FinalCode;
     _FinalCode.open("../FinalCode/FinalCode.cpp", ios::out);
     
    /*yydebug = 1;*/

    string input = cleanedCode.str();

    input.erase(remove_if(input.begin(), input.end(), isspace), input.end());
    set_input_string(input.c_str());


    code << "#include <iostream>"<< endl << "using namespace std;" << endl << "int main()" << endl << "{" << endl;

    yyparse();
    
    code << "return 0;" << endl;
    code << '}' << endl;

    cout << code.str();


    if (_FinalCode.is_open())
    {
        _FinalCode << code.str();
        code.flush();
        _FinalCode.flush();
    }
    return 0;
}