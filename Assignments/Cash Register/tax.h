#pragma once
#include <iostream>
#include <string>
#include <sstream>

class Items {
private:
	int quantity;
	std::string itemName, txt;
	bool imported;
	float cost, tax, total;

public:
	Items() {
		quantity = 0;
		itemName = " ";
		imported = false;
		cost = 0.0;
		tax = 0.0;
		total = 0.0;
		txt = " ";
	}

	Items(std::string line) {
		quantity = 0;
		itemName = " ";
		imported = false;
		cost = 0.0;
		tax = 0.0;
		total = 0.0;
		txt = line;
	}

	void newLine(std::string line) {
		txt = line;
		setQuantity();
		setItemName();
		setImported();
		setCost();
		setTax();
		setTotal();
	}
	void setQuantity() {
		bool end = false;
		std::string num = "a";
		int counter = 0;

		do {
			if (txt[counter] != ' ') {
				if (num == "a")
					num = txt[counter];
				else
					num = num + txt[counter];
			}
			else
				end = true;
			counter++;
		} while (!end);

		int q;
		std::istringstream(num) >> q;
		quantity = q;

	}
	void setItemName() {
		setImported();
		std::string n;

		int counter = 0;
		while (txt[counter] == '1' || txt[counter] == '2' || txt[counter] == '3' || txt[counter] == '4'
			|| txt[counter] == '5' || txt[counter] == '6' || txt[counter] == '7' || txt[counter] == '8' ||
			txt[counter] == '9' || txt[counter] == '0' || txt[counter] == ' ')
			counter++;
		if (imported)
			counter += 9;
		n = txt[counter];

		while (txt[counter] != ' ' && txt[counter + 1] != 'a' && txt[counter + 2] != 't')
			n = n + txt[counter];

	}
	void setImported() {
		int counter = 0;
		while (txt[counter] == '1' || txt[counter] == '2' || txt[counter] == '3' || txt[counter] == '4'
			|| txt[counter] == '5' || txt[counter] == '6' || txt[counter] == '7' || txt[counter] == '8' ||
			txt[counter] == '9' || txt[counter] == '0' || txt[counter] == ' ')
			counter++;

		std::string find;
		find = txt[counter];
		for (int i = 0; i < 8; i++)
			find = find + txt[counter];

		if (find == "imported")
			imported = true;
		else
			imported = false;
	}
	void setCost() {
		int counter = 0;
		std::string n;

		while (txt[counter] != 'a' && txt[counter + 1] != 't')
			counter++;
		counter += 3;

		n = txt[counter];
		counter++;
		while (txt[counter] != '.') {
			n = n + txt[counter];
			counter++;
		}

		n = n + txt[counter]; // .
		n = n + txt[counter + 1]; // decimal
		n = n + txt[counter + 2]; // decimal 2

		float c;
		std::istringstream(n) >> c;
		cost = c;

	}
	void setTax() {
		bool taxed = false;
		
		std::size_t found = txt.find("book");
		if (found != std::string::npos)
			taxed = true;
		found = txt.find("books");
		if (found != std::string::npos)
			taxed = true;
		found = txt.find("pill");
		if (found != std::string::npos)
			taxed = true;
		found = txt.find("pills");
		if (found != std::string::npos)
			taxed = true;
		found = txt.find("chocolate");
		if (found != std::string::npos)
			taxed = true;
		found = txt.find("chocolates");
		if (found != std::string::npos)
			taxed = true;
		
		if (taxed == true)
			tax = 0.0;
		else
			tax = (cost * .10);

		if (imported)
			tax = tax + (cost * .05);
		else
			tax = tax + 0;
		


	}
	void setTotal() {
		total = cost + tax;
	}

	int getQuantity() {
		return quantity;
	}
	std::string getItemName() {
		return itemName;
	}
	bool getImported() {
		return imported;
	}
	float getCost() {
		return cost;
	}
	float getTax() {
		return tax;
	}
	float getTotal() {
		return total;
	}

};