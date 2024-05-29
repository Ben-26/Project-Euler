#include<iostream>
#include<cmath>

uint64_t integerSqrt(uint64_t x); // If x is a perfect square, return its root, otherwise return 1


// Not functional 

int main() {
	int n = 285;
	bool found = false;
	uint64_t P, H;


	while (!found) {
		n++;
		P = integerSqrt(12 * n * (n + 1) + 1);
		H = integerSqrt(4 * n * (n + 1) + 1);
		if (P % 6 == 5 && H % 4 == 3) {
			found = true;
		}
	}
	std::cout << n * (n + 1) / 2 << std::endl;

	return 0;
}

uint64_t integerSqrt(uint64_t x) {
	if (x < 0) {
		std::cout << "Negative input \n\n\n\n\n\n" << std::endl;
		return false;
	}

	uint64_t low = 0;
	uint64_t high = x;

	while (low <= high) {
		uint64_t mid = (high + low) / 2;
		uint64_t midSquared = mid * mid;

		if (midSquared == x) {
			return mid;
		}
		else if (midSquared < x) {
			low = mid + 1;
		}
		else {
			high = mid - 1;
		}
	}
	return 1; // all numbers are greater than 41, 1 mod 6 != 5 and 1 mod 4 != 3
}
