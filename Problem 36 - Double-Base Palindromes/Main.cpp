#include <iostream>
#include <vector>

std::vector<int> toVector(unsigned int x);
bool palindrome(std::vector<int> digits);
std::vector<int> toBinary(unsigned int x);

int main() {

	
	unsigned int sum = 0;
	for (unsigned int i = 0; i < 1000000; i++) {
		if (palindrome(toVector(i)) && palindrome(toBinary(i))) {
			sum += i;
		}
	}
	std::cout << sum;
	

	return 0;
}

std::vector<int> toVector(unsigned int x) {
	unsigned int numDigits = trunc(log10(x)) + 1;
	std::vector<int> digits;
	//std::cout << x << " has " << trunc(log10(x)) + 1 << " digits" << std::endl;
	for (int i = 0; i < numDigits; i++) {
		digits.push_back(x % 10);
		x = (x - (x % 10)) / 10;
	}
	return digits;
}

bool palindrome(std::vector<int> digits){
	for (int i = 0; i < digits.size(); i++) { // can be more efficient
		//std::cout << "Comparing " << digits.at(i) << " with " << digits.at(digits.size() - i - 1) << std::endl;
		if (digits.at(i) != digits.at(digits.size() - i - 1)) {
			return false;
		}
	}
	return true;
}

std::vector<int> toBinary(unsigned int x) {
	int binaryDigits = trunc(log2(x));
	std::vector<int> binary;
	for (int i = binaryDigits; i >= 0; i--) {
		if (x - pow(2, i) >= 0) {
			binary.push_back(1);
			x -= pow(2, i);
		}
		else {
			binary.push_back(0);
		}
	}
	return binary;
}
