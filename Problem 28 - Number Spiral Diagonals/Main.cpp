#include <iostream>

/*
For side length n, NW corner = (2n + 1) ^ 2
Corner difference = 2n
*/ 

int main() {
	int side_max = 1001;
	int n = 1;
	int sum = 1;

	while (2 * n + 1 <= side_max) {
 		sum += 4 * (2 * n + 1) * (2 * n + 1) - 12 * n;
		n++;
	}
	std::cout << sum;

	return 0;
}
