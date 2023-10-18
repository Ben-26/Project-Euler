#include <iostream>
#include <vector>

std::vector<int> f(int n); // Recursively calculates 2^n  [ max n = 1887 ] 
std::vector<int> g(std::vector<int> v); // Doubles the input digit vector 


int main() {
	std::vector<int> v = f(1000);
	int t = 0;
	for (int i = v.size() - 1; i >= 0; i--) {
		std::cout << v.at(i); // Debug 
		t += v.at(i);
	}
	std::cout << "\n" << std::endl; // Debug 
	std::cout << t << std::endl;

	return 0;
}

std::vector<int> f(int n) {
	if (n == 1) {
		return std::vector<int> {2};
	}
	else {
		return g(f(n - 1));
	}
}

std::vector<int> g(std::vector<int> v) { 
	int carry = 0;
	for (int i = 0; i < v.size(); i++) {
		v.at(i) *= 2;
		if (carry == 1) {
			v.at(i) += 1;
			carry = 0;
		}
		if (v.at(i) >= 10) {
			v.at(i) -= 10;
			carry = 1;
		}
	}
	if (carry == 1) {
		v.push_back(1);
	}
	return v;
}