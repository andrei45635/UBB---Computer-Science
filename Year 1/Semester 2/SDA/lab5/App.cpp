#include <iostream>

#include "TestExtins.h"
#include "TestScurt.h"

using namespace std;


int main() {
	cout << "Beginning testing...\n";
	testAll();
	cout << "Finished the short test...\n";
	testAllExtins();
	cout << "Finished the extended test...\n";
	cout << "Finished both tests!\n";
}
