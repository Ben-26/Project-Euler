#include <iostream>
#include <vector>

std::vector <std::vector<int>> pAlg(std::vector<std::vector<int>> S);
unsigned int intFactorial(unsigned int x);
unsigned int toInt(std::vector<int> S);

int main() {
	std::vector<std::vector<int>> perm = pAlg({ {}, {0,1,2,3,4,5,6,7,8,9} });
	std::vector<int> primes = { 2,3,5,7,11,13,17 };
	//std::vector<std::vector<int>> perm = { {1,4,0,6,3,5,7,2,8,9} };
	
	unsigned long int sum = 0;
	for (unsigned int i = 0; i < perm.size(); i++) {
		int x = 0;
		for (int j = 1; j < 8; j++) {
			std::vector<int> substring = std::vector<int>(perm.at(i).begin() + j, perm.at(i).begin() + j + 3);
			//std::cout << toInt(substring) << " % " << primes.at(j - 1) << " = " << toInt(substring) % primes.at(j - 1) << "\n";
			x += toInt(substring) % primes.at(j - 1);
		}
		if (!x) {
			std::cout << toInt(perm.at(i)) << "\n";
			sum += toInt(perm.at(i));
		}
	}

	std::cout << "sum: (incorrect)" << sum;// Manually adding outputs gives correct sum 

	return 0;
}

unsigned int toInt(std::vector<int> S) {
	unsigned int sum = 0;
	for (int i = 0; i < S.size(); i++) {
		sum += S.at(i) * pow(10, S.size() - i - 1);
	}
	return sum;
}

std::vector<std::vector<int>> pAlg(std::vector <std::vector<int>> S) {
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
			for (int i = 0; i < intFactorial(N); i++) { // Current set
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

unsigned int intFactorial(unsigned int x) {
	return x > 1 ? x * intFactorial(x - 1) : (x == 0 or x == 1 ? 1 : 0);
}