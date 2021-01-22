#include "StringCleanup.h"
#include <vector>

string StringCleanup::Cleanup(string input)
{
    //Functions need to run in this order. Please don't change else output will be incorrect.
    StringCleanup::RemoveComments(input);
    StringCleanup::RemoveEmptyLines(input);
    StringCleanup::RemoveExtraSpace(input);
    StringCleanup::InsertNeccessarySpace(input);
    StringCleanup::RemoveLeadingSpace(input);
    

    return input;
}

bool StringCleanup::IsIdentify(string input)
{
    char firstChar = input.at(0);

    if (isdigit(firstChar))
        return false;

    int i = 1;
    while (input[i])
    {
        char c = input[i];

        if (!isdigit(c) &&
            !isalpha(c) &&
            c != '_' &&
            isspace(c))

            return false;
        i++;
    }
}

bool StringCleanup::BothAreSpaces(char lhs, char rhs) { return (lhs == rhs) && (lhs == ' '); }
bool StringCleanup::BothAreTabs(char lhs, char rhs) { return (lhs == rhs) && (lhs == '\t'); }

void StringCleanup::RemoveExtraSpace(string& input)
{
    string::iterator new_end = std::unique(input.begin(), input.end(), StringCleanup::BothAreSpaces);
    input.erase(new_end, input.end());
}

void StringCleanup::RemoveEmptyLines(string& input)
{
    istringstream str(input);
    string line;
    string final;

    while (getline(str, line))
    {
        if (!line.empty())
            final.append(line + "\n");
    }

    input = final;
}

void StringCleanup::RemoveLeadingSpace(string& input)
{
    bool flag = true;
    while(flag)
    {
        auto found = input.find("\n ");
        if (found != string::npos)
        {
            input.replace(found, 2, "\n");
        }
        else
            flag = false;
    }
}

void StringCleanup::RemoveComments(string& input)
{
    string final;
    bool comment = false;
    for (int i = 0; i < input.length(); i++)
    {
        if (input[i] == '(' && input[i + 1] == '*')
            comment = true;
        else if (input[i] == '*' && input[i + 1] == ')')
        {
            comment = false;
            i++;
            continue;
        }
            


        if (comment == false)
            final.push_back(input[i]);
    }

    input = final;
}

void StringCleanup::InsertNeccessarySpace(string& input)
{
    string final;
    string FixedQuote;
    bool quote = false;
    for (int i = 0; i < input.length(); i++)
    {
        if (input[i] == '\'')
            quote = !quote;

        if (input[i] == '=' && quote == false)
        {
            if (!isspace(input[i - 1]))
                final.push_back(' ');
                
            if (!isspace(input[i + 1]))
            {
                final.push_back(input[i]);
                final.push_back(' ');
                ++i;
            }
        }

        if (isspace(input[i]) && quote == false)
            if (input[i + 1] == ';' || input[i + 1] == ',')
                ++i;

        if (input[i] == ',' && quote == false)
            if (!isspace(input[i + 1]))
            {
                final.push_back(input[i]);
                final.push_back(' ');
                ++i;
            }
                

        final.push_back(input[i]);
    }  
    input = final;
}




