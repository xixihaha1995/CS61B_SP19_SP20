#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main()
{

    string mystr;
    int i, r, sum=0;

    cout << "enter a number\n";
    getline(cin, mystr);
    stringstream(mystr) >> i;
    while(i>0)  
    {
        r = i % 10;
        sum += r;
        i /= 10;
    }
    
    cout << "all the digits"<< sum << endl;

}
