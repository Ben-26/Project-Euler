#include <iostream>
#include <vector>

bool LtR(unsigned int x);// Checks prime from left to right 
bool RtL(unsigned int x);// Checks prime from right to left
bool prime(int x);

int main() {	
	int primesFound = 0;
	int i = 8;
	unsigned int sum = 0;
	while (primesFound != 11) {
		if (LtR(i) && RtL(i)) {
			primesFound += 1;
			std::cout << i << "  is a truncatable prime  " << std::endl;
			sum += i;
		}
		i++;
	}
	std::cout << sum;
	return 0;
}

bool LtR(unsigned int x) {
	if (x == 0) {
		return true;
	}
	unsigned int y = trunc(log10(x));
	return prime(x) ? LtR(x - pow(10, y) * trunc(x / pow(10, y))) : false;
}

bool RtL(unsigned int x) {
	if (x == 0) {
		return true;
	}
	return prime(x) ? RtL((x - (x % 10)) / 10) : false;
}

bool prime(int x) {
	if (x == 2 or x == 3) {
		return true;
	}
	else if (x <= 1 or x % 2 == 0 or x % 3 == 0) {
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