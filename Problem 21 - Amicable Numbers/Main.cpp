#include <iostream>

int d(int n); // Sum of proper divisors of n

int main() {
	int t = 0;
	for (int a = 1; a < 10000; a++) {
		int b = d(a);
		if (a == d(b) && a != b) {
			t += a;
		}
	}
	std::cout << t;
	return 0;
}

int d(int n) {
	int t = 0;
	for (int i = 1; i < n; i++) {
		if (n % i == 0) {
			t += i;
		}
	}
	return t;
}