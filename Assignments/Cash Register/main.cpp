#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "tax.h"
using namespace std;


void readText(string, int);

int main() {
	// Input 1
	cout << "INPUT 1:\n";
	readText("Input1.txt", 1);

	// Input 2
	cout << "INPUT 2:\n";
	readText("Input2.txt", 2);

	// Input 3
	cout << "INPUT 3:/n";
	readText("Input3.txt", 3);


	return 0;
}

void readText(string n, int i) {
	ifstream textFile;
	string line;
	vector<Items> itemList;
	Items temp;

	textFile.open(n);

	if (textFile.is_open()) {
		while (getline(textFile, line)) {
			cout << line << endl;
			temp.newLine(line);
			cout << temp.getCost();
			itemList.push_back(temp);
		}
		cout << endl;

		textFile.close();
		cout << "OUTPUT " << i << ":\n";

		float runningTotalTax = 0.0;
		float runningTotal = 0.0;
		for (int i = 0; i < itemList.size(); i++) {
			cout << itemList[i].getQuantity() << " ";
			if (itemList[i].getImported())
				cout << "imported";
			cout << " " << itemList[i].getItemName() << " at " << itemList[i].getTotal() << endl;
			runningTotalTax += itemList[i].getTax();
			runningTotal += itemList[i].getTotal();
		}
		
		cout << "Sales Tax: " << runningTotalTax << endl;
		cout << "Total: " << runningTotal << endl;
	}
	else
		cout << "Unable to open file.";
	

}
