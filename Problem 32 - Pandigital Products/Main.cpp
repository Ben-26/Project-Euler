#include <iostream>
#include <vector>

std::vector <std::vector<int>> pAlg(std::vector <std::vector<int>> S);// Permutates the input set S			NOTE: Input as {{} , {set to permutate}} 
unsigned int factorial(unsigned int x); // Returns x!
int multiplyVec(std::vector<int> S, unsigned int mltp, unsigned int mlpc); // Returns 0 if the product is equal to the multiplicand and the multiplier
bool inCache(std::vector<int> cache, int search); // Returns true if the search value is within the cache


int main() {
	std::vector<int> digits = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	std::vector<int> cache;


	
	std::vector <std::vector<int>> P = pAlg({ {}, digits}); // Permutations 
	for (unsigned int i = 1; i < P.size(); i++) {
		for (unsigned int j = 1; j < 5; j++) {
			for (unsigned int k = 0; k < 5; k++) {
				int product = multiplyVec(P.at(i), j, k);
				if (!inCache(cache, product)) {
					cache.push_back(product);
				}
			}
		}
	}

	unsigned int sum = 0; 
	for (unsigned int i = 0; i < cache.size(); i++) {
		sum += cache.at(i);
	}
	std::cout << sum;
	

	//std::cout << multiplyVec({ 3,9,1,8,6,7,2,5,4 }, 2, 3);



	
	return 0;
}

bool inCache(std::vector<int> cache, int search) {
	for (int i = 0; i < cache.size(); i++) {
		if (cache.at(i) == search) {
			return true;
		}
	}
	return false;
}

int multiplyVec(std::vector<int> S, unsigned int mltp, unsigned int mlpc) { // mltp = multiplier size,		mlpc = multiplicand size
	int multiplier = 0;
	int multiplicand = 0;
	int product = 0;
	for (int i = 0; i < mltp; i++) {
		multiplier += S.at(i) * pow(10, mltp - i - 1);
	}
	for (int j = 0; j < mlpc; j++) {
		multiplicand += S.at(j + mltp) * pow(10, mlpc - j - 1);
	}
	for (int k = 0; k < S.size() - (mltp + mlpc); k++) {
		product += S.at(k + mltp + mlpc) * pow(10, S.size() - (mltp + mlpc) - k - 1);
	}
	//std::cout << "Multiplier = " << multiplier << "\nMultiplicand = " << multiplicand << "\nProduct = " << product << std::endl;
	//std::cout << "Multipler size = " << mltp << " Multiplicand size = " << mlpc << " Product size " << S.size() - (mltp + mlpc) << "\n" << std::endl;
	if (multiplier * multiplicand == product) {
		return product;
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





