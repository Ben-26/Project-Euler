#include <iostream>

int main() {
	int c = 0; // Prime counter
	int x = 2; // Current number 
	bool prime = true;
	while (c < 10001) {
		// Prime check 
		for (int i = 2; i < x; i++) {
			if ((x % i) == 0) {
				prime = false;
			}
		}
		if (prime) {
			c += 1;
		}
		prime = true;
		x += 1;
	}
	std::cout << "Prime number " << c << " = " << x - 1 << std::endl;
}