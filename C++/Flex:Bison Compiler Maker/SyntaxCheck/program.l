%option noyywrap

%{
#include <stdio.h>
#include <string.h>
#include "program.tab.h"
void showError();
%}

numbers     ([0-9])+
abcdef      ([a-fA-F])+
string      \"(\\.|[^"\\])*\"

%%
INTEGER     {yylval.c = _strdup(yytext); return INTEGER;}
PROGRAM     {yylval.c = _strdup(yytext); return PROGRAM;}
VAR         {yylval.c = _strdup(yytext); return VAR;}
BEGIN       {yylval.c = _strdup(yytext); return BEGINCOPY;}
PRINT       {yylval.c = _strdup(yytext); return PRINT;}
END         {yylval.c = _strdup(yytext); return END;}
"."         {yylval.c = _strdup(yytext); return DOT;}
")"         {yylval.c = _strdup(yytext); return CLOSEPAR;}
"("         {yylval.c = _strdup(yytext); return OPENPAR;}
"/"         {yylval.c = _strdup(yytext); return DEVIDE;}
"*"         {yylval.c = _strdup(yytext); return MULTIPLY;}
"-"         {yylval.c = _strdup(yytext); return SUBTRACT;}
"+"         {yylval.c = _strdup(yytext); return ADD;}
"="         {yylval.c = _strdup(yytext); return EQUAL;}
";"         {yylval.c = _strdup(yytext); return SEMICOLON;}
":"         {yylval.c = _strdup(yytext); return COLON; }
","         {yylval.c = _strdup(yytext); return COMMA; }
{numbers}   {yylval.c = _strdup(yytext); return digit;}
{abcdef}    {yylval.c = _strdup(yytext); return abcdef;}
{string}    {yylval.c = _strdup(yytext); return str;}
.           {return *yytext; }
%%
void showError(){
    printf("WRONG INPUT!!!");
}
void set_input_string(const char* in) {
  yy_scan_string(in);
}

void end_lexical_scan(void) {
  yy_delete_buffer(YY_CURRENT_BUFFER);
}