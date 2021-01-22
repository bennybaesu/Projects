#include "Menu.h" // iostream is in Menu.h
#include "Double.h"


int main()
{
    int numDie; // The number of dice the user will use
    std::cout << "Welcome to the PIG game!" << std::endl << std::endl;
    Menu menu; // Creates a menu object so the user can choose their choice

    bool valid;
    do
    {
	   std::cout << "Enter the number of die you want to use: ";
	   std::cin >> numDie; // User inputs the number of dice
	   valid = std::cin.good();

	   if ((numDie >= 1 && numDie <= 20) && valid)
		  break;
	   else
	   {
		  std::cout << "Invalid Entry, try again!" << std::endl;
		  std::cin.clear();
	   }
    } while (true);

    if (menu.getGameMode() == 1) // If user chooses 1, it creates a Core object
	   Core core(numDie);
    else if (menu.getGameMode() == 2)
	   Double dub(numDie); // If user chooses 2, it creates a Double object (multiplayer)
}
