#include <iostream>
#include <vector>
#include <fstream>
#include <string>

int main() {
	std::ifstream my_file("triangle.txt");
	std::string numbers = "";
	while (my_file) {
		char c;
		my_file >> c;
		numbers = numbers + c;
	}
	std::cout << numbers << std::endl; // Amount of numbers too large to fit into single string

	std::vector<std::vector<int>> tri;

	int nRows = sqrt(0.25 + numbers.length()) + 0.5;
	int c = 0;
	std::cout << "length: " << numbers.length() << " n rows:" << nRows << std::endl;
	for (int i = 1; i < nRows; i++) {
		std::vector<int> row;
		for (int j = 0; j < i; j++) {
			std::cout << 10 * (numbers[c] - 48) + numbers[c + 1] - 48 << " ,";
			row.push_back(10 * (numbers[c] - 48) + numbers[c + 1] - 48);
			c += 2;
			std::cout << "c = " << c << std::endl;
		}
		tri.push_back(row);
	}
	//std::cout << "\n";

	// Debug 
	for (int i = 0; i < tri.size(); i++) {
		for (int j = 0; j < tri.at(i).size(); j++) {
			std::cout << tri.at(i).at(j) << " ,";
		}
		std::cout << " " << std::endl;
	}
	std::cout << "\n";


	int t = tri.at(0).at(0); // Total
	int i = 1; // Current row
	int j = 0; // Current path 
	int br_1, br_2; // Left and Right branch 
	while (i < nRows - 2) {
		br_1 = tri.at(i + 1).at(j) > tri.at(i + 1).at(j + 1) ? j : j + 1;
		br_2 = tri.at(i + 1).at(j + 1) > tri.at(i + 1).at(j + 2) ? j + 1 : j + 2;
		if (tri.at(i).at(j) + tri.at(i + 1).at(br_1) > tri.at(i).at(j + 1) + tri.at(i + 1).at(br_2)) {
			std::cout << "+" << tri.at(i).at(j) << std::endl;
			t += tri.at(i).at(j);
		}
		else {
			t += tri.at(i).at(j + 1);
			j++;
		}
		i++;
	}
	if (tri.at(i).at(j) > tri.at(i).at(j + 1)) {
		t += tri.at(i).at(j);
	}
	else {
		t += tri.at(i).at(j + 1);
	}

	std::cout << t;


	return 0;
}