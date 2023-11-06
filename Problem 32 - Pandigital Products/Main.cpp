#include <iostream>
#include <vector>

std::vector <std::vector<int>> pAlg(std::vector <std::vector<int>> S);// Permutates the input set S			NOTE: Input as {{} , {set to permutate}} 
unsigned int factorial(unsigned int x); // Returns x!


int main() {
	std::vector<int> digits = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };


	std::vector <std::vector<int>> P = pAlg({ {}, {1, 2, 3, 4} }); // Permutations 
	for (unsigned int i = 0; i < P.size(); i++) {
		for (int j = 0; j < 4; j++) {//Multiplicand
			for (int k = 0; k < 4; k++) {//Multiplier 
				
			}
		}
	}
	
	return 0;
}

unsigned int factorial(unsigned int x) {
	return x > 1 ? x * factorial(x - 1) : (x == 0 or x == 1 ? 1 : 0);
}

std::vector <std::vector<int>> pAlg(std::vector <std::vector<int>> S) {
	int N = S.at(0).size();
	if (S.at(S.size() - 1).size() == 0) {
		S.pop_back();
		return S;
	}
	else {
		int X = S.at(S.size() - 1).at(S.at(S.size() - 1).size() - 1); // Gets the last element of the last vector
		S.at(S.size() - 1).pop_back();
		std::vector<std::vector<int>> pSet;

		if (N == 0) {
			std::vector<int> temp;
			temp.push_back(X);
			pSet.push_back(temp);
			pSet.push_back(S.at(S.size() - 1));
		}
		else {
			for (int i = 0; i < factorial(N); i++) { // Current set
				for (int j = 0; j < N + 1; j++) { // Index to insert X at
					std::vector<int> subset;
					for (int k = 0; k < N; k++) { // Index of the elements from the current set
						if (j == k) {
							subset.push_back(X);	
						}
						subset.push_back(S.at(i).at(k));
					}
					if (j == N) { // Deals with the final set not pushing X 
						subset.push_back(X);
					}
					pSet.push_back(subset);
				}
				
			}
			pSet.push_back(S.at(S.size() - 1));
		}
		return pAlg(pSet);
	}
}





