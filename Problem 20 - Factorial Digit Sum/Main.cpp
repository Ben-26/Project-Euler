#include <iostream>
#include <vector>

std::vector<int> factorial(int n); // Returns n!
std::vector<int> multiplier(int n, std::vector<int> x); // Returns n * x 
std::vector<int> sum(std::vector<int> a, std::vector<int> b); // Returns a + b

int main() {
	std::vector<int> digits = factorial(100);
	int t = 0;
	for (int i = digits.size() - 1; i >= 0; i--) {
		//std::cout << digits.at(i) << " ";
		t += digits.at(i);
	}
	std::cout << t << std::endl;
	return 0;
}

std::vector<int> factorial(int n) {
	if (n == 1) {
		return std::vector<int> {1};
	}
	else {
		return multiplier(n, factorial(n - 1));
	}
}

std::vector<int> multiplier(int n, std::vector<int> x) {
	std::vector<int> y = x;
	for (int i = 0; i < n - 1; i++) {
		y = sum(x, y);
	}
	return y;
}

std::vector<int> sum(std::vector<int> a, std::vector<int> b) {
	int carry = 0;
	std::vector<int> sum = a.size() > b.size() ? a : b; // Larger of the two inputs
	std::vector<int> smaller = a.size() > b.size() ? b : a; // Smaller of the two inputs
	int d = sum.size() - smaller.size();
	for (int i = 0; i < d; i++) {
		smaller.push_back(0);
	}
	for (int i = 0; i < sum.size(); i++) {
		sum.at(i) += smaller.at(i);
		if (carry == 1) {
			sum.at(i)++;
			carry = 0;
		}
		if (sum.at(i) >= 10) {
			sum.at(i) -= 10;
			carry = 1;
		}
	}
	if (carry == 1) {
		sum.push_back(1);
	}
	return sum;
}
