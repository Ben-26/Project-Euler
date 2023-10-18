#include <iostream>

int main() {
	//int a, b, c;
	for (int a = 1; a < 1000; a++) {
		for (int b = 1; b < 1000; b++) {
			for (int c = 1; c < 1000; c++) {
				if (((a + b + c) == 1000) && (pow(a, 2) + pow(b, 2) == pow(c, 2))) {
					std::cout << "a = " << a << ", b =  " << b << ", c = " << c << ", a * b * c = " << a * b * c << std::endl;
				}
			}
		}
	}
}