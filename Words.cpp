#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {
	string fn = argv[1];
    vector<string> everyWord;
    vector<string> eachWord;
    vector<int> numWord;
    int startInt = 1;
    string temp;
    ifstream fin;
    fin.open(fn);
    while (fin && fin.peek() != EOF) {
        getline(fin, temp, ' ');
        everyWord.push_back(temp);
    }
    fin.close();
    bool validation = true;
    // loop through everyword and add one of each word to the vector
    for(int i = 0; i < everyWord.size(); i++){
         for(int j = 0; j < eachWord.size(); j++){
             // if it is not already in eachWord
             if(everyWord[i] == eachWord[j]){
                 numWord[j] += 1;
                 validation = false;
             }
         }
         if(validation){
             eachWord.push_back(everyWord[i]);
             numWord.push_back(startInt);
         }
         validation = true;
    }

    ofstream fout;
    fout.open("numOfWords_" + fn);
    if(numWord.size() == eachWord.size()){
        for(int i = 0; i < eachWord.size(); i++){
            fout << eachWord[i] << ": " << numWord[i] << endl;
        }
    }
}