#include <iostream>
#include <random>

/*
 * The function for generating random 
 * numbers in a given range
 * @param a, b The boundaries of the range for generating a random number
 * @return x The generated random number from the random function
 */
int random(int a, int b) {
    std::random_device random_device;
    std::mt19937 generator(random_device());
    std::uniform_int_distribution<> segment(a, b);
    int x = segment(generator);
    return x;
}

/*
 * The function for generating a random s equence of
 * bits of a given length and displaying it on the screen
 * @param n The number of bits in the sequence 
 */
void RandomGenerator(int n) {
    for(int i = 0; i < n; i++) 
        std::cout << random(0, 1);
}

int main() {
    const int NUMBER = 128;
    RandomGenerator(NUMBER);
    return 0; 
}