#pragma once
#include "Core.h"
using namespace std;


class Double : public Core
{
private:
    int roundPoints;
    int numPlayers;
    Core* player;
    bool winner;

public:
    Double(); // Default Constructor
    Double(int); // Constructor
    ~Double(); // Destructor

    void game(); // The multiplayer game happens here
    void displayRules(); // Displays the rules to the users

    void setRoundPoints(int, int); // Sets the points for that round
    void setPlayers(); // Gets the number of players playing
};


//******************************************************************************
// FUNCTION DEFENITIONS:
//******************************************************************************
Double::Double()
{
    numDie = 0;
    totalPoints = 0;
    highScore = 0;
    numPlayers = 2;
    tries = 1;
    maximum = 100;
    rollOne = false;
    turn = true;
    winner = false;

    die = new Die[numDie];
    snakeEyes = new bool[numDie];
    player = new Core[numPlayers];

    for (int i = 0; i < numDie; i++)
    {
	   snakeEyes[i] = false;
    }
    for (int j = 0; j < numPlayers; j++)
    {
	   player[j] = (Core(numDie, true));
    }

}

Double::Double(int num)
{
    maximum = 100;
    numDie = num;
    setPlayers();
    totalPoints = 0;
    turn = true;
    rollOne = false;
    winner = false;

    die = new Die[numDie];
    snakeEyes = new bool[numDie];
    player = new Core[numPlayers];

    for (int i = 0; i < numDie; i++)
    {
	   snakeEyes[i] = false;
    }
    for (int j = 0; j < numPlayers; j++)
    {
	   player[j] = (Core(numDie, true));
    }

    setMax();
    displayRules();
    game();
}

Double::~Double()
{
    delete[] die;
    delete[] snakeEyes;

    die = NULL;
    snakeEyes = NULL;
}

void Double::setPlayers()
{
    int choice;
    do
    {
	   cout << "You are set on 2 player mode. Press 1 to continue or 2 to add players: ";
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
	   numPlayers = 2;
    else if (choice == 2)
    {
	   cin.clear();
	   do
	   {
		  cout << "Enter the number of players: ";
		  cin >> choice;
		  valid = cin.good();

		  if ((choice >= 2 && choice <= 10) && valid)
			 break;
		  else
		  {
			 cout << "Invalid Entry! Try again\n";
			 cin.clear();
		  }
	   } while (true);
	   numPlayers = choice;
    }
}

void Double::displayRules()
{
    cout << endl << endl;

    char anyKey;

    cout << "MULTIPLAYER RULES:" << endl;
    cout << "During a player's turn, the player will roll their dice." << endl;
    cout << "The numbers the dice land on will be added to the player's total." << endl;
    if (numDie == 1)
	   cout << "If the die lands on 1, the player will lose the points accumulated for that round and lose their turn." << endl;
    else
    {
	   cout << "If one of the die lands on 1, the player will lose their points for that round and lose their turn." << endl;
	   cout << "If all of the dice land on 1, the player will lose ALL of their points." << endl;
	   cout << "The first person to make it to " << maximum << " wins." << endl;
    }

    cout << "Press any key, then enter, to continue... ";
    cin >> anyKey;
    cout << endl << endl;
}

void Double::game()
{
    int count; // To keep a count of total points for subtraction later to get roundPoints
    for (int i = 0; i < numPlayers; i++) // For loop for each player's turn
    {
	   count = player[i].getTotalPoints();
	   turn = true;
	   cout << "PLAYER " << i + 1 << endl;
	   do
	   {

		  player[i].Turn();
		  setRoundPoints(i, count);


		  if (player[i].getRollOne() == true && (player[i].SnakeEyes() == false || player[i].getNumDie() == 1))
		  {
			 cout << "One of your die landed on 1, you lose your turn!" << endl;
			 cout << "You lost your " << roundPoints << " points. ";
			 player[i].setTotalPoints(count);
			 cout << "Your total is currently: " << player[i].getTotalPoints() << endl;
			 player[i].setTurn(false);
		  }
		  else if (player[i].getRollOne() == true && player[i].SnakeEyes() == true && player[i].getNumDie() != 1)
		  {
			 cout << "All of your dice landed on 1! You lose all of  your points." << endl;
			 player[i].setTotalPoints(0);
			 player[i].setTurn(false);
		  }
		  else if (player[i].getRollOne() == false && player[i].SnakeEyes() == false)
		  {
			 if (player[i].getTotalPoints() >= maximum)
				winner = true;

			 if (winner == false)
			 {
				cout << "CURRENT POINTS: " << roundPoints << endl;
				cout << "TOTAL POINTS: " << player[i].getTotalPoints() << endl;
				player[i].rollAgain();
			 }

		  }
		  cout << endl;
		  if (winner == true)
			 break;

	   } while (player[i].getTurn() == true); // End of do-while loop
	   count = NULL;
	   roundPoints = NULL;


	   if (i == (numPlayers - 1)) // If it gets to the last player, i becomes -1 so that it become 0 when the loop iterates
		  i = -1;
	   if (winner == true)
	   {
		  char anyKey;
		  cout << "Player " << i + 1 << " is a winner! Game over." << endl;
		  cout << "Press any key and enter to end game: ";
		  cin >> anyKey;
		  break;
	   }

    } // End of the for loop
}

void Double::setRoundPoints(int j, int count)
{
    roundPoints = player[j].getTotalPoints() - count;
}
