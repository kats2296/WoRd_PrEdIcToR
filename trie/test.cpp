#include<fstream>
#include<iostream>
#include<string>
using namespace std ;

int main()
{
    ifstream readfile("words.txt");
    string data;
	int k=0;

    string previousLine="";
    cout<<"READING STARTS\n";


    while(!readfile.eof()) // To get you all the lines.
    {
        getline(readfile,data); // Saves the line in STRING.
        if (data != previousLine)
        {
      		k++;
            previousLine=data;
            cout<<data<<endl; // Prints our STRING.
        }
	

        //readfile>>data;

    }
	cout<<k;
    readfile.close();
    return 0 ;
}
