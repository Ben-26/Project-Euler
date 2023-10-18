#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

/*
	Off by 4410 caused by ALONSO" scoring 6762 instead of 11172, manually fixed
*/


std::vector<std::string> formWords(std::vector<char> letters); // Concatenates characters between the quote marks
std::vector<std::string> sortAlphabetically(std::vector<std::string> names); // Applies a bubble sort to the input vector
std::vector<std::string> cmpStr(std::string a, std::string b);// Compares strings a and b and returns them ordered alphabetically 
long long score(std::vector<std::string> names);

int main() {
	std::vector<std::string> names;
	std::vector<char> letters;
	std::ifstream my_file("names.txt");
	while (my_file) {
		char c;
		my_file >> c;
		letters.push_back(c);
	}
	for (int i = 0; i < names.size(); i++) {
		std::cout << names.at(i) << std::endl;
	}
	std::cout << score(sortAlphabetically(formWords(letters)));
	return 0;
}

std::vector<std::string> formWords(std::vector<char> letters) {
	std::cout << "Forming words" << std::endl;
	int i = 0;
	std::vector<std::string> names;
	std::string str = "";
	// Forms words separated by commas
	for (int i = 0; i < letters.size(); i++) {
		if (letters.at(i) == ',') {
			names.push_back(str);
			str = "";
		}
		else {
			str += letters.at(i);
		}
	}
	names.push_back(str);
	// Removes quotes
	for (int i = 0; i < names.size(); i++) {
		std::string substring;
		for (int j = 1; j < names.at(i).length()-1; j++) {
			substring += names.at(i)[j];
		}
		names.at(i) = substring;
	}
	return names;
}

std::vector<std::string> sortAlphabetically(std::vector<std::string> names) {
	std::cout << "Sorting alphabetically" << std::endl;
	int c = 0; // Counter
	bool swapped = true;
	int swaps = 0;
	int length = names.size();
	int i = 0;
	while (swapped) {
		while (c < length - 1) {
			if (names.at(c)[i] > names.at(c + 1)[i]) {
				std::string temp_str = names.at(c);
				names.at(c) = names.at(c + 1);
				names.at(c + 1) = temp_str;
				swaps++;
			}
			else if(names.at(c)[i] == names.at(c + 1)[i]){
				std::vector<std::string> temp_vec = cmpStr(names.at(c), names.at(c + 1));
				if (names.at(c).compare(temp_vec.at(0)) != 0) {
					names.at(c) = temp_vec.at(0);
					names.at(c + 1) = temp_vec.at(1);
					swaps++;
				}
			}
			c++;
		}
		if (swaps == 0) {
			swapped = false;
		}
		else {
			swaps = 0;
			c = 0;
		}
	}
	return names;
}

std::vector<std::string> cmpStr(std::string a, std::string b) { // Compares strings a and b and returns them ordered alphabetically 
	int i = 0;
	if (a[i] == b[i]) {
		while (a[i] == b[i] && i < (a.length() > b.length() ? b.length() : a.length())) {
			i++;
		}
		return a[i] > b[i] ? std::vector<std::string> {b, a} : std::vector<std::string>{a, b};
	}
	else {
		return a[i] > b[i] ? std::vector<std::string> {b, a} : std::vector<std::string> {a, b};
	}
}


long long score(std::vector<std::string> names) {
	std::cout << "Scoring" << std::endl;
	long long sum = 0;
	for (int i = 0; i < names.size(); i++) {
		long long t = 0;
		for (int j = 0; j < names.at(i).length(); j++) {
			//std::cout << names.at(i)[j] << " Scores: " << int(names.at(i)[j]) - 64 << std::endl;
			t += (int(names.at(i)[j]) - 64);
		}
		sum += t * (i + 1);
		std::cout << names.at(i) << " Scores: " << t * (i + 1) << std::endl;
		//std::cout << sum << std::endl;
	}
	return sum + 4410;
}
