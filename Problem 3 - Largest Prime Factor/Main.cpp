#include <iostream>

int main() {
	long long n = 600851475143;
	//int n = 13195;
	int max = 1; 
	int factor;
	bool prime;

	for (long long i = 1; i < ceil(n/2); i++) {
		// Factor Check 
		if ((n % i) == 0) {
			prime = true;
			factor = n / i;

			// Checks if the factor is prime 
			for (int j = 2; j < factor; j++) {
				if ((factor % j) == 0) {
					prime = false;
				}
			}
			std::cout << "Factor:" << factor << " Prime? " << prime <<std::endl;
			if ((prime == true) && (factor > max)){
				max = factor;
			}
		}
	}
	std::cout << max << std::endl;

	return 0;
}