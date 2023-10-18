#include <iostream>

int main() {
	int x_nSub1 = 1;
	int x_n = 2;
	int x_nPlus1 = x_n + x_nSub1;
	int c = 0; // Counter 

	while (x_nPlus1 < 4000000) {
		x_nPlus1 = x_n + x_nSub1;
		std::cout << x_nPlus1 << std::endl;
		x_nSub1 = x_n;
		x_n = x_nPlus1; 
		if ((x_nPlus1 % 2) == 0) {
			c += x_nPlus1;
		}
	}
	std::cout << c << std::endl;


	return 0;
}