#include <iostream>

// Janky asf 

int div(long long x);

int main() {
	long long n = 1;// 13500
	int d_max = 0;
	while (div(n * (n+1) / 2) <= 500) {
		std::cout << "<-  Triangle num: " << n * (n + 1) / 2 << std::endl;
		n++;
	}
	std::cout << "\n" << n * (n + 1) / 2 << std::endl;
}

int div(long long x) {
	int d = 0;
	for (long long i = 1; (i * i) <= x; i++) {
		if ((x % i) == 0) {
			if (i * i < x) {
				d += 2;
			}
			else {
				d += 1;
			}
		}
	}
	std::cout << d; 
	return d;
}


