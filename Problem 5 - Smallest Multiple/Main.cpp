#include <iostream>

int main() {
	int i = 1, j = 1;
	while (j <= 20) {
		if ((i % j) == 0) {
			j += 1;
		}
		else {
			j = 1;
			i += 1;
		}
	}
	std::cout << i << std::endl;
	return 0;
}