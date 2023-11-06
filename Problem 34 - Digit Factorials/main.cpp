#include <iostream>

unsigned int factorial(unsigned int x);
unsigned int sumDigitsFactorial(unsigned int x);

int main() {
	unsigned int sum = 0;
	for (unsigned int i = 3; i < 7*factorial(9); i++) {
		if (i == sumDigitsFactorial(i)) {
			sum += i;
		}
	}
	std::cout << sum;
	return 0; 
}

unsigned int factorial(unsigned int x) {
	return x >= 2 ? x * factorial(x - 1) : (x == 0 or x == 1 ? 1 : 0);
}

unsigned int sumDigitsFactorial(unsigned int x){
	unsigned int sum = 0; 
	for (int i = 0; i < trunc(log10(x)) + 1; i++) {
		sum += factorial((x % (int)pow(10, i + 1)) / pow(10, i));
		x -= x % (int)pow(10, i + 1);
	}
	return sum;
}
