#pragma once
#include <cstdlib> // To get random numbers
#include <ctime>


class Die
{
private:
    int result; // The number the die lands on
    int sides; // The number of sides of the die

public:
    Die();

    int getSides();
    int getResult();

    void roll();
};

//******************************************************************************
// FUNCTION DEFENITIONS:
//******************************************************************************
Die::Die()
{
    result = 1;
    sides = 6;
}

int Die::getSides()
{
    return sides;
}

int Die::getResult()
{
    return result;
}

void Die::roll()
{
    srand(time(0));
    int random = rand();
    srand(random);
    result = (rand() % 6) + 1;
}


