#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main()
{

    string mystr;
    float price = 0;
    int quantity=0;

    cout << "enter price\n";
    getline(cin, mystr);
    stringstream(mystr) >> price;
    cout << "enter quantity\n";
    getline(cin, mystr);
    stringstream(mystr) >> quantity;
    cout << "total price:" << quantity*price << endl;
}
