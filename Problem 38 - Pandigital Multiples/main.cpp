#include <iostream>
#include <vector>
#include <string> 

bool pandigital(unsigned int x);
std::vector<int> bubbleSort(std::vector<int> S);

int main() {
	unsigned int max = 0;
	for (int i = 2; i < 10000; i++) {
		int j = 2;
		std::string concat = std::to_string(i);
		while ((concat + std::to_string(i * j)).size() <= 9) {
			concat += std::to_string(i * j);
			j++;
		}
		if (concat.size() == 9 && pandigital(std::stoi(concat))) {
			if (std::stoi(concat) > max) {
				max = std::stoi(concat);
			}
		}
	}

	std::cout << max;

	return 0;
}

bool pandigital(unsigned int x) {
	std::vector<int> S;
	int size = (int)log10(x) + 1;
	for (int i = 0; i < size; i++) {
		S.push_back(x % 10);
		x = (x - x % 10) / 10;
	}
	return bubbleSort(S) == std::vector<int>{1, 2, 3, 4, 5, 6, 7, 8, 9} ? true : false;
}

std::vector<int> bubbleSort(std::vector<int> S) {
	int i = 0;
	int swaps = 0;
	bool swapped = true;
	int length = S.size();
	while (swapped) {
		while (i < length - 1) {
			if (S.at(i) > S.at(i + 1)) {
				int temp = S.at(i);
				S.at(i) = S.at(i + 1);
				S.at(i + 1) = temp;
				swaps++;
				}
			i++;
		}
		if (!swaps) {
			swapped = false;
		}
		else {
			swaps = 0;
			i = 0;
		}
	}
	return S;
}