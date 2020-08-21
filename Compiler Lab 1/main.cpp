#include <iostream>
#include <fstream>
#include<vector>

using namespace std;

bool checkKeywords(const string &user_input);

bool checkIdentifier(const string &user_input);

void printList(const vector<string> &v);

int main() {
    string user_input;
    cout << "Enter Your String For Check: ";
    getline(cin, user_input);

    bool ck_key = checkKeywords(user_input);
    cout << "Inspection Results" << endl;
    if (!ck_key) {
        cout << "The given string is NOT a Keyword." << endl;
        bool ck_ident = checkIdentifier(user_input);
        if (ck_ident) {
            cout << "It is a VALID identifier." << endl;
        } else {
            cout << "It is NOT a valid identifier" << endl;
        }
    } else {
        cout << "The given string is a Keyword." << endl;
        cout << "It is NOT a valid identifier.";
    }
    return 0;
}

bool checkIdentifier(const string &user_input) {

    if (user_input[0]) {
        int check_ascii = int(user_input[0]);
        if (check_ascii <= 57 and check_ascii >= 47) {
            return false;
        }
    }

    for (const auto &x: user_input) {

        int check = int(x);

        if (check == 95) {
            continue;
        } else if ((check >= 65 and check <= 90) or (check >= 97 and check <= 122)) {
            continue;
        } else if (check <= 57 and check >= 47) {
            continue;
        } else {
            return false;

        }
    }

    return true;
}

bool checkKeywords(const string &user_input) {
    string word;  // for reading input from the file
    vector<string> keywordsList;
    ifstream file;
    file.open("/home/inan/CLionProjects/Compiler Lab 1/keywords.txt");  // Open the file of keywords
    if (!file) {
        cerr << "Unable to open file keywords.txt for some error!";
        exit(1);   // call system to stop
    } else {
        while (file >> word) {
            keywordsList.push_back(word); // make a list of keywords
        }
    }
    file.close(); // close the file
    // printList(keywordsList);

    for (const auto &check:keywordsList) {
        if (check == user_input) {
            return true;
        }
    }
    return false;
}

void printList(const vector<string> &v) {
    for (const auto &x: v) {
        cout << x << endl;
    }
}