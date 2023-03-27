#include <iostream>

#include "TestScurt.h"
#include "TestExtins.h"

int main() {
    std::cout << "Beginning testing..." << std::endl;
       testAll();
       std::cout << "Finished short test!" << std::endl;
       testAllExtins();
    std::cout << "Finished both tests!" << std::endl;
}
