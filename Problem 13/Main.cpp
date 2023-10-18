#include <iostream>
#include <fstream>
#include <cmath>

int main() {
	int arr[100][50], deg[50];
	long long sum = 0;
	std::ifstream my_file("numbers.txt");


	// Fill array of digits
	for (int i = 0; i < 100; i++) {
		char c;
		for (int j = 0; j < 50; j++) {
			my_file >> c;
			arr[i][j] = (int)c - 48;
		}
	}

	// Adds the digits individually , array pos n corresponds to 10^(50 - n)
	for (int i = 0; i < 50; i++) {
		deg[i] = 0;
		for (int j = 0; j < 100; j++) {
			deg[i] += arr[j][i];
			
		}
		std::cout << deg[i] << std::endl; // Debug
	}
	
	std::cout << "\n" << std::endl; // Debug

	int x = 0;
	while (log10(sum) < 12) {
		sum = sum * 10 + deg[x];
		std::cout << sum << std::endl; // Debug
		x += 1;
	}

	std::cout << "\n Digits: " << sum / 1000 << std::endl;

	return 0;
}