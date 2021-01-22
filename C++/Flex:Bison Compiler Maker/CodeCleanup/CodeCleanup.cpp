// CPSC323Project.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include "StringCleanup.h"

int main()
{
    fstream _file;
    _file.open("code.txt", ios::out | ios::in);

    stringstream code;

    if (_file.is_open())
    {
        code << _file.rdbuf();
        _file.flush();
    }
    
    ofstream  f;
    f.open("../SyntaxCheck/CleanedCode.txt");

    StringCleanup cleanup = StringCleanup();

    string cleanCode = cleanup.Cleanup(code.str());
    f << cleanCode;
    std::cout << cleanCode;
}
