#pragma once
#include <string>
#include <algorithm>
#include <cctype>
#include <sstream>

using namespace std;
class StringCleanup
{
public:
	string Cleanup(string);
private:
	static bool BothAreSpaces(char, char);
	static bool BothAreTabs(char, char);
	void RemoveExtraSpace(string&);
	void RemoveLeadingSpace(string&);
	void InsertNeccessarySpace(string&);
	bool IsIdentify(string);
	void RemoveComments(string&);
	void RemoveEmptyLines(string&);
};

