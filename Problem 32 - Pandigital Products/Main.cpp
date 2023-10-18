
#include <iostream>
#include <vector>

bool duplicate(std::vector<unsigned int> set, unsigned int value); // Returns true if the value is already within the set

int main() {
	std::vector<unsigned int> cache; // Pandigital numbers
	std::vector<unsigned int> digitSet = { 1, 2, 3, 4, 5, 6, 7, 8, 9 }; // Needed ?

	return 0;
}

bool duplicate(std::vector<unsigned int> set, unsigned int value) {
	for (int i = 0; i < set.size(); i++) {
		if (set.at(i) == value) {
			return true;
		}
	}
	return false;
}





