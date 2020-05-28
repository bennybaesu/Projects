#pragma once
#include "Die.h"
#include <iostream>
#include <string>
#include <limits>
using namespace std;

class Menu
{
private:
    int gameMode; // Single player or Multiplayer
    bool valid;

public:

    Menu(); // Default Constructor

    void setGameMode(int);
    int getGameMode();
    void display(); // Displays the menu

    class Error
    {
    private:
	   string msg;
	   int value;

    public:
	   Error() {}
	   Error(string msg, int value)
	   {
		  this->msg = msg;
		  this->value = value;
	   }
	   string GetError()
	   {
		  return msg;
	   }

	   int GetData()
	   {
		  return value;
	   }
    };
};


//******************************************************************************
// FUNCTION DEFENITIONS:
//******************************************************************************

Menu::Menu()
{
    int choice;

    display(); // Displays the menu to the user
    cin >> choice; // User inputs their choice here
    valid = cin.good();
    try
    {
	   if (valid == true)
		  setGameMode(choice);
	   else
		  setGameMode(0);
    }
    catch (Menu::Error error)
    {
	   cout << "ERROR: " << error.GetError() << endl;
	   cin.clear();
	   cin.ignore(std::numeric_limits<streamsize>::max(), '\n');

	   Menu();
    }
}

void Menu::display()
{
    cout << "MENU:" << endl;
    cout << "[1] - Single Player Mode" << endl;
    cout << "[2] - Multiplayer Mode" << endl;
    cout << "Enter Choice: ";
}


void Menu::setGameMode(int mode)
{
    if (mode != 1 && mode != 2)
    {
	   throw(Error("That is not one of the choices. Try again: \n", mode));
    }
    else
	   gameMode = mode;
}

int Menu::getGameMode()
{
    return gameMode;
}
