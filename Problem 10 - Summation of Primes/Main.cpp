#include <iostream>

bool primeCheck(int n);

int main() {
	long long x = 2; // Current number 
	long long sum = 0;
	while(x < 2000000) {
		if (primeCheck(x)) {
			sum += x;
		}
		x += 1;
	}
	std::cout << sum << std::endl;
}

bool primeCheck(int n) {
	if (n == 2 || n == 3) {
		return true;
	}
	if (n <= 1 || n % 2 == 0 || n % 3 == 0){
		return false;
	}
	for (int i = 5; i * i <= n; i += 6){
		if (n % i == 0 || n % (i + 2) == 0)
			return false;
	}
	return true;
}
