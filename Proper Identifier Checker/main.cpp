/*
 AUTHOR: Benjamin Baesu
 DATE: Feb 20, 2020
 
 PROGRAM: Check if a user inputted string is a proper identifier. If string starts with digit, it is invalid. If string contains any characters besides letters, digits, or underscores, it is invalid.
 */


#include <iostream>
#include <string>
using namespace std;

bool isDigit(char c)
{
    if(c == '0')
        return true;
    else if(c == '1')
        return true;
    else if(c == '2')
        return true;
    else if(c == '3')
        return true;
    else if(c == '4')
        return true;
    else if(c == '5')
        return true;
    else if(c == '6')
        return true;
    else if(c == '7')
        return true;
    else if(c == '8')
        return true;
    else if(c == '9')
        return true;
    else
        return false;
}

bool validChar(char c)
{
    if(c == 'a' || c == 'b' || c == 'c' || c == 'd' || c == 'e' || c == 'f' || c == 'g' ||
       c == 'h' || c == 'i' || c == 'j' || c == 'k' || c == 'l' || c == 'm' || c == 'n' ||
       c == 'o' || c == 'p' || c == 'q' || c == 'r' || c == 's' || c == 't' || c == 'u' ||
       c == 'v' || c == 'w' || c == 'x' || c == 'y' || c == 'z')
        return true;
    
    else if(c == 'A' || c == 'B' || c == 'C' || c == 'D' || c == 'E' || c == 'F' || c == 'G' ||
       c == 'H' || c == 'I' || c == 'J' || c == 'K' || c == 'L' || c == 'M' || c == 'N' ||
       c == 'O' || c == 'P' || c == 'Q' || c == 'R' || c == 'S' || c == 'T' || c == 'U' ||
       c == 'V' || c == 'W' || c == 'X' || c == 'Y' || c == 'Z')
        return true;
    
    else if(c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6'
            || c == '7' || c == '8' || c == '9' || c == '_')
        return true;
    else return false;
}


bool checkString(string s)
{
    // If first character is a digit
    if(isDigit(s[0]))
        return false;
    
    // Check if the rest of the characters are valid
    for(int i = 0; i < s.length(); i++)
    {
        if(!validChar(s[i]))
            return false;
    }
    return true;
}

void getString()
{
    string userInput = "";
    bool cont = false;
    
    cout << "Enter a string: ";
    getline(cin, userInput);
    
    if(checkString(userInput))
        cout << userInput << " is an identifier.\n";
    else
        cout << userInput << " is not an identifier.\n";
    
    do{
        cin.clear();
        cout << "Do you want to enter another string? (y/n): ";
        getline(cin, userInput);
        if (userInput != "Y" && userInput != "y" && userInput != "n" && userInput != "N"){
            cout << "Invalid input. Try again.\n";
            cont = false;
        }
        else
            cont = true;
    } while (cont == false);
    
    if (userInput == "y" || userInput == "Y")
        getString();
}


int main()
{
    getString();
    return 0;
}
