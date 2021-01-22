
#pragma once
#include "Die.h"
#include <iostream>
#include <Windows.h>
#include <limits>
using namespace std;

class Core
{
protected:
    Die * die;
    bool* snakeEyes;
    bool rollOne, turn, valid;
    int totalPoints, maximum, numDie, highScore, tries;

public:
    Core();
    Core(int);
    Core(int, bool);
    ~Core();

    void game();
    void Turn();
    void displayRules();
    void rollAgain();
    bool SnakeEyes();

    void setMax();
    void setHighScore();
    void setTurn(bool);
    void setTotalPoints(int);

    int getTotalPoints();
    int getNumDie();
    bool getTurn();
    bool getRollOne();

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
Core::Core()
{
    numDie = 0;
    totalPoints = 0;
    highScore = 0;
    tries = 1;
    maximum = 100;
    rollOne = false;
    turn = true;
    die = new Die[numDie];
}

Core::Core(int num)
{
    numDie = num;
    die = new Die[num];
    snakeEyes = new bool[num];
    totalPoints = 0;
    turn = true;
    rollOne = false;
    setMax();
    displayRules();
    game();
    tries = 1;
    highScore = 0;
}

Core::Core(int num, bool multi)
{
    numDie = num;
    die = new Die[num];
    snakeEyes = new bool[num];
    totalPoints = 0;
    turn = true;
    rollOne = false;
    tries = 1;
    highScore = 0;
}

Core::~Core()
{
    delete[] die;
    delete[] snakeEyes;

    die = NULL;
    snakeEyes = NULL;
}


void Core::game()
{
    do
    {
	   Turn();
	   cout << "CURRENT TOTAL: " << totalPoints << endl;

	   if (rollOne == true)
	   {
		  cout << "One of your die landed on 1! Round over" << endl;
		  setHighScore();
		  tries++;
		  cout << "You made it to " << totalPoints << " points." << endl;
		  cout << "Your High Score was: " << highScore << endl;
		  totalPoints = 0;
		  turn = false;
		  rollAgain();
	   }

	   else if (totalPoints >= maximum && rollOne == false)
	   {
		  cout << "You made it to " << maximum << " points! Congrats!" << endl;
		  cout << "It took you " << tries << " tries." << endl;
		  turn = false;
		  setHighScore();
	   }
	   else if (rollOne == false && totalPoints < maximum)
		  rollAgain();



    } while (turn == true);
}

void Core::Turn()
{
    rollOne = false;
    cout << "Rolling..." << endl;

    for (int i = 0; i < numDie; i++)
    {
	   die[i].roll();
	   cout << "Die " << i + 1 << " landed on: " << die[i].getResult() << endl;
	   totalPoints += die[i].getResult();
	   Sleep(1000);

	   if (die[i].getResult() == 1)
	   {
		  rollOne = true;
		  if (numDie != 1) // Only lets snakeEyes happen if there is more than 1 die
			 snakeEyes[i] = true;
	   }
	   else
		  snakeEyes[i] = false;
    }
} // END TURN FUNCTION

void Core::displayRules()
{
    char anyChar;
    cout << endl << "SINGLE PLAYER MODE:" << endl;

    cout << "Roll your dice until you get to " << maximum << endl;

    cout << "If one of your die lands on 1, you lose. How many tries will it take you to get to " << maximum << "? Have fun!" << endl;

    cout << "Press any key and enter to continue: ";
    cin >> anyChar;
}

void Core::rollAgain()
{
    int choice;
    do
    {
	   cout << "Would you like to roll again? Enter 1 for yes or 2 for no: ";
	   cin >> choice;
	   valid = cin.good();
	   if ((choice == 1 || choice == 2) && valid)
		  break;
	   else
	   {
		  cout << "Invalid Entry! Try again\n";
		  cin.clear();
	   }
    } while (true);


    if (choice == 1)
	   turn = true;
    else if (choice == 2)
    {
	   turn = false;
	   cout << "Turn over. Score: " << totalPoints << endl;
    }
}

bool Core::SnakeEyes()
{
    bool trueFalse = true;
    for (int i = 0; i < numDie; i++)
    {
	   if (snakeEyes[i] != 1) // If one of the die doesn't equal 1, player doesn't lose all their points
		  trueFalse = false;
    }

    return trueFalse; // Returns true or false
}


void Core::setMax()
{
    int choice;

    do
    {
	   cout << "Your goal is currently 100 points. Press 1 to continue or 2 to change the goal: ";
	   cin >> choice;
	   valid = cin.good();

	   if ((choice == 1 || choice == 2) && valid)
		  break;
	   else
	   {
		  cout << "Invalid Entry. Please try again\n";
		  cin.clear();
	   }
    } while (true);



    if (choice == 1)
	   maximum = 100;
    if (choice == 2)
    {
	   int choice;
	   do
	   {
		  cout << "Enter a goal score: ";
		  cin >> choice;
		  valid = cin.good();

		  if ((choice >= (maximum * numDie) && choice <= 1000) && valid)
			 break;
		  else
		  {
			 cout << "Invalid Entry! Try again\n";
			 cin.clear();
		  }

	   } while (true);

	   maximum = choice;
    }
}

void Core::setHighScore()
{
    if (totalPoints >= highScore)
	   highScore = totalPoints;
}

void Core::setTurn(bool turn)
{
    this->turn = turn;
}

void Core::setTotalPoints(int i)
{
    totalPoints = i;
}


int Core::getTotalPoints()
{
    return totalPoints;
}

int Core::getNumDie()
{
    return numDie;
}

bool Core::getTurn()
{
    return turn;
}

bool Core::getRollOne()
{
    return rollOne;
}
