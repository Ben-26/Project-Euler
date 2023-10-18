#include <iostream> 

int main() {
	int x = 0;
	int y = 0;

	for (int i = 1; i <= 100; i++) {
		x += pow(i, 2);
		y += i;
	}
	std::cout << pow(y, 2) - x << std::endl;
}