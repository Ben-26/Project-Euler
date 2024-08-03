
#include <iostream>

int gcd(int a, int b) {
	while (b != 0) {
		int temp = b;
		b = a % b;
		a = temp;
	}
	return a;
}

int main() {
	int counter = 0;

	for (int d = 2; d <= 12000; d++) {
		for (int n = int(d / 3) + 1; n <= int(d / 2); n++) {
			counter += int(gcd(n, d) == 1);
		}
	}
	std::cout << counter - 1;

	return 0;
}