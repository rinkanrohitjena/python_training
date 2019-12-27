// Example program
#include <iostream>
#include <string>

int main()
{
    std::string name;
    std::cout << "What is your name? ";
    getline(std::cin, name);
    std::cout << "Hello, " << name << "!\n";
}
g++ helloworld.cpp - o helloworld && "/root/Desktop/python/" helloworld