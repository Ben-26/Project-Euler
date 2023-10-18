#include <iostream>
#include <vector>

unsigned int sumDigits(unsigned int x); // returns the sum of the 5th powers of the digits of x

int main(){
	unsigned int sum = 0;
	for (unsigned int i = 2; i < 999999; i++) {
		if (i == sumDigits(i)) {
			sum += i;
		}
	}
	std::cout << sum;
	return 0;
}

unsigned int sumDigits(unsigned int x) {
	int digits = trunc(log10(x)) + 1;
	unsigned int sum = 0;
	for (int i = 0; i <= digits; i++) {
		unsigned int cache = trunc(x / pow(10, digits - i));
		x -= cache * pow(10, digits - i);
		sum += pow(cache, 5);
	}
	return sum;
}