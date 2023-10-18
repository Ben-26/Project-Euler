#include <iostream>
#include <vector>

std::vector<int> sum(std::vector<int> a, std::vector<int> b);

int main() {
	std::vector<std::vector<int>> F = { {1}, {1}, {2} }; // Circular queue

	int i = 0;
	while (F.at(i % 3).size() < 1000) {
		F.at(i % 3) = sum(F.at((i + 1) % 3), F.at((i + 2) % 3));
		i++;
	}
	std::cout << i + 1; // Not sure why +1
	return 0;
}

std::vector<int> sum(std::vector<int> a, std::vector<int> b) {
	std::vector<int> r = a.size() > b.size() ? a : b; // Result
	std::vector<int> s = a.size() > b.size() ? b : a; // Smaller of the two inputs
	int carry = 0;
	int d = r.size() - s.size();
	for (int i = 0; i < d; i++) {
		s.push_back(0);
	}
	for (int i = 0; i < r.size(); i++) {
		r.at(i) += s.at(i);
		if (carry == 1) {
			r.at(i)++;
			carry = 0;
		}
		if (r.at(i) >= 10) {
			r.at(i) -= 10;
			carry = 1;
		}
	}
	if (carry == 1) {
		r.push_back(1);
	}
	return r;
}
