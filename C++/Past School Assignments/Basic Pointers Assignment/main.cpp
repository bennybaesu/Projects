#include <iostream>
using namespace std;

void display(int, double[], double);

int main()
{
    int numDays; // The number of days that the user enters
    double* days = NULL; // To get started with the dynamic array
    double wage; // The hours worked and the wage
    
    cout << "Enter the number of days you have worked this pay period: ";
    cin >> numDays; // User enters the number of days they have worked
    
    cout << "Enter your hourly wage rate: $";
    cin >> wage;
    
    cout << endl; // Skip a line
    
    days = new double[numDays]; // Dynamically allocate the days array
    
    for(int i = 0; i < numDays; i++) // Loop to fill array
    {
        cout << "How many hours did you work on DAY " << i + 1  << "? ";
        cin >> days[i];
    }
    
    display(numDays, days, wage); // Calls display function
    
    delete [] days; // Deallocates the days array
    days = NULL; // Sets the days pointer equal to nothing
    
} // End main


void display(int size, double array[], double wage)
{
    double hours = 0; // Keeps a total of the hours
    
    for(int i = 0; i < size; i++)
    {
        cout << "Day " << i + 1 << ": " << array[i] << " hours ($" << array[i] * wage << ")" << endl;
        hours += array[i]; // Adds the day's hours to the running total
    }
    
    double total = hours * wage; // Adds up the total net income
    cout << "Your net income this pay period is $" << total << endl;
}