#include <iostream>

unsigned int factorial(unsigned int x);
unsigned int sumDigits(unsigned int x);

int main() {
	unsigned int sum = 0;

	std::cout << sumDigits(123);

	for (unsigned int i = 3; i < 7*factorial(9); i++) {
		if (i == sumDigits(i)) {
			sum += i;
		}
	}
	std::cout << sum;
	return 0; 
}

unsigned int factorial(unsigned int x) {
	return x == 2 ? 2 : x * factorial(x - 1);
}

unsigned int sumDigits(unsigned int x) {
	unsigned int sum = 0;
	for (int i = log10(x) + 1; i > 0; i--) {
		sum += factorial(floor(x / pow(10, i)));
	}
	return sum;
}