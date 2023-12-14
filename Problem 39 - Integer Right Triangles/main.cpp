#include <iostream>

int main() {
	int max = 0;
	
	for (int p = 1; p <= 1000; p++) {
		int counter = 0;
		for (int a = 1; a < p / 2; a++) {
			for (int b = 1; b < p / 2; b++) {
				for (int c = 1; c < p / 2; c++) {
					if((a + b + c == p) && (a * a + b * b == c * c)) {
						counter++;
					}
				}
			}
		}
		if (counter > max) {
			max = p;
		}
	}
	std::cout << max;

	return 0;
}