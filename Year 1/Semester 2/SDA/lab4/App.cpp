#include "TestExtins.h"
#include "TestScurt.h"


#include <iostream>
using namespace std;


int main() {
	testAll();
	cout << "Passed short test!\n";
	testAllExtins();
	cout << "Passed extended test!\n";
	cout << "That's all!" << endl;
	return 0;
}

