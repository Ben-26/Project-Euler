#include <iostream>
#include <vector>

bool palindrome(unsigned int x);


int main() {
	unsigned int x = 123454321;
	std::cout << "\n" << x << " is a palindrome ? " << palindrome(x);

	/*
		unsigned int sum = 0;
	for (unsigned int i = 0; i < 1000000; i++) {
		if (palindrome(i) && palindrome(toBinary(i))) {
			sum += i;
		}
	}
	std::cout << sum;
	*/

	return 0;
}

bool palindrome(unsigned int x){
	unsigned int numDigits = trunc(log10(x)) + 1;
	std::vector<unsigned int> digits;
	//std::cout << x << " has " << trunc(log10(x)) + 1 << " digits" << std::endl;
	for (int i = 0; i < numDigits; i++) {
		digits.push_back(x % 10);
		x = (x - (x % 10)) / 10;
	}
	

	for (int i = 0; i < digits.size(); i++) { // can be more efficient
		//std::cout << "Comparing " << digits.at(i) << " with " << digits.at(digits.size() - i - 1) << std::endl;
		if (digits.at(i) != digits.at(numDigits - i - 1)) {
			return false;
		}
	}
	return true;
}

unsigned int toBinary(unsigned int x) {
	return 0;
}
