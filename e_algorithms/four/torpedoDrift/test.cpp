//
// Created by Alec Mirambeau on 3/12/24.
//

#include <iostream>

int main() {
    int number1, number2;

    // Prompt the user to enter two numbers separated by a space
    std::cout << "Enter two numbers separated by a space: ";

    // Read the input from the user
    std::cin >> number1 >> number2;

    // Output the numbers entered by the user
    std::cout << "You entered: " << number1 << " and " << number2 << std::endl;

    return 0;
}
