//  Program to convert temperature from Celcius degree
//  units into Fahrenheit degree units:
//  Fahrenheit = Celsius * (212 - 32/100 + 32)

//#include <stdio.h>
#include <iostream>

using namespace std;

int main(int nNumberofArgs, char* pszArgs[])
{
    // enter the temperature in Celsius
    int celcius;
    cout << "Enter the temperature in Celsius:";
    cin >> celcius;

    // calculate conversion factor for Celsius
    // to Fahrenheit
    int factor;
    factor = 212 - 32;

    // use conversion factor to convert Celsius
    // into Fahrenheit values
    int fahrenheit;
    fahrenheit = factor * celcius/100 + 32;

    // output the results
    cout << "Fahrenheit value is:";
    cout << fahrenheit;

    return 0;

}