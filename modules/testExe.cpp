#include <iostream>
#include <string>

int main(int argc, char **argv){
    std::cout << "Hello" << std::endl;
    std::cout << "Argument count: " << argc << std::endl;

    for(unsigned int a = 0; a < argc; a++){
        std::cout << a << "\t" << argv[a] << std::endl;
    }

    return 0;
}