#include <iostream>
#include <vector>

unsigned int calc_chain(int a, int b); // returns the prime chain created by the two coefficients
bool prime(int n); // Returns whether a number is prime or not

int main() {
	int chain_max = 0;

	
	std::vector<int> coeff; // a , b

	for (int a = -999; a < 1000; a++) {
		for (int b = -999; b < 1000; b++) {
			unsigned int chain = calc_chain(a, b);
			if (chain > chain_max) {
				chain_max = chain;
				coeff = { a, b };
			}
		}
	}
	std::cout << coeff.at(0) * coeff.at(1);
	return 0;
}

unsigned int calc_chain(int a, int b) {
	unsigned int n = 0;
	while (prime(n * (n + a) + b)){
		n++;
	}
	return n;
}

bool prime(int n){
	if (n == 2 || n == 3) {
		return true;
	}
	if (n <= 1 || n % 2 == 0 || n % 3 == 0) {
		return false;
	}
		
	for (int i = 5; i * i <= n; i += 6)
	{
		if (n % i == 0 || n % (i + 2) == 0) {
			return false;
		}		
	}
	return true;
}
