#include <iostream>
#include <vector>

bool prime(int x); // Returns true if prime
int circular(int p); // Returns 1 if circular and 0 if not 

int main() {
	unsigned int counter = 0;
	std::vector<int> primeCache;
	for (unsigned int i = 2; i < 1000000; i++) {
		if (prime(i)) {
			primeCache.push_back(i);
		}
	}

	for (unsigned int i = 0; i < primeCache.size(); i++) {
		counter += circular(primeCache.at(i));
	}
	std::cout << counter;
	return 0;
}

int circular(int p) {
	int digits = trunc(log10(p)) + 1;
	int next = p;
	for (int i = 0; i < digits; i++) {
		next = (next % 10) * pow(10, digits - 1) + (next - (next % 10)) / 10;
		if(!prime(next)) {
			return 0;
		}
	}
	return 1;
}

bool prime(int x) {
	if (x == 2 or x == 3) {
		return true;
	}
	else if ( x <= 1 or x % 2 == 0 or x % 3 == 0){
		return false;
	}
	else {
		for (int i = 5; i * i <= x; i++) {
			if (x % i == 0 or x % (i + 2) == 0) {
				return false;
			}
		}
		return true;
	}

}