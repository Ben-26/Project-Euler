#include <iostream>
#include <vector>

std::vector<int> genAbundant(int limit); // Generates a vector of all abundant numbers below the limit
bool checkAbundant(int num); // Checks whether the number is abundant, returns true if it is and false if it isnt
int getIndex(std::vector<int> v, int limit); // Returns the index of the first number below the inputted limit 

int main() {
	const int limit = 28123;
	int total = 0;
	std::vector<int> abundant = genAbundant(limit);
	std::vector<int> sums;

	for (int i = 0; i < limit; i++) {
		sums.push_back(0);
	}
	/* Theoretically faster
	int min = 0;
	int max;
	for (int j = 0; j < getIndex(abundant, int(limit / 2)); j++) {
		max = getIndex(abundant, limit - abundant.at(j));
		for (int i = min; i < max; i++) {
			sums.at(abundant.at(i) + abundant.at(j)) = abundant.at(i) + abundant.at(j);
		}
		min++;
	}
	
	*/

	for (int i = 0; i < abundant.size(); i++) {
		for (int j = 0; j < abundant.size(); j++) {
			int x = abundant.at(i) + abundant.at(j);
			if (x < limit) {
				sums.at(x) = x;
			}
		}
	}

	for (int i = 0; i < sums.size(); i++) {
		if (sums.at(i) == 0) {
			total += i;
		}
	}
	std::cout << total;
	return 0;
}

int getIndex(std::vector<int> v, int limit) {
	for (int i = v.size() - 1; i > 0; i--) {
		if (v.at(i) < limit) {
			return i;
		}
	}
	return v.size() - 1;
}

std::vector<int> genAbundant(int limit) {
	std::vector<int> a;
	for (int i = 1; i < limit; i++) {
		if (checkAbundant(i)) {
			a.push_back(i);
		}
	}
	return a;
}

bool checkAbundant(int num) {
	if (num == 1) {
		return false;
	}
	int n = ceil(sqrt(num));
	int total = 1;
	int d = 2; // divisor
	while (d < n) {
		if (num % d == 0) {
			total += d;
			total += num / d;
		}
		d++;
	}
	if (n * n == num) {
		total += n;
	}
	return total > num ? true : false;
}