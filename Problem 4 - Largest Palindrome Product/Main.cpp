#include <iostream>
#include <cmath>
#include <string>

bool pCheck(long long i); // Returns whether the number is a palindrome 

int main() {
	long long max = 0;
	for (int i = 100; i < 1000; i++) {
		for (int j = 100; j < 1000; j++) {
			long long prod = i * j;
			if ((prod > max) && (pCheck(prod))) {
				max = prod;
			}
		}
	}
	std::cout << max << std::endl;
	return 0;
}

bool pCheck(long long i) {
	bool r = true;
	std::string s = std::to_string(i);
	int d = trunc(log10(i) + 1); // Number of digits 
	for (int i = 0; i < d / 2; i++){ 
		if (s[i] != s[d - i - 1]) {
			r = false;
		}
	}
	return r;
}