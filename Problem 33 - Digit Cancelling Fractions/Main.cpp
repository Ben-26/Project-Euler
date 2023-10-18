#include <iostream>
#include <vector>

unsigned int gcd(int a, int b); // returns the greatest common divisor of a and b
std::vector<int> digitCancel(unsigned int a, unsigned int b); // if a = 49 and b = 98 -> returns 4/8

int main() {
	unsigned int numProd = 1;
	unsigned int denomProd = 1;

	for (int a = 10; a < 100; a++) {
		for (int b = 10; b < 100; b++) {
			if ((a / gcd(a, b)) / (b / gcd(a, b)) == digitCancel(a, b).at(0) / digitCancel(a, b).at(1)) {
				numProd *= a;
				denomProd *= b;
			}
		}
	}
	std::cout << "Unsimplified" << numProd << " / " << denomProd;

	return 0;
}

unsigned int gcd(int a, int b) {
	unsigned int max = 0;

	return max;
}

std::vector<int> digitCancel(unsigned int a, unsigned int b) {


}


/*
Let some fraction, a/b have a simplified form c/d
suppose a is in the form cx or xc 
suppose b is int he form dx or xd
Then a/b meets the criteria
*/