#pragma once
#include "NumGoblin.h"

// Functions
unsigned int nGob::intFactorial(unsigned int x) {
	return x > 1 ? x * intFactorial(x - 1) : (x == 0 or x == 1 ? 1 : 0);
}


// Algorithms
std::vector<std::vector<int>> nGob::pAlg(std::vector <std::vector<int>> S) {
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

bool nGob::palindrome(std::vector<int> digits) {
	for (int i = 0; i < digits.size(); i++) { // can be more efficient
		if (digits.at(i) != digits.at(digits.size() - i - 1)) {
			return false;
		}
	}
	return true;
}

bool nGob::prime(int x) {
	if (x == 2 or x == 3) {
		return true;
	}
	else if (x <= 1 or x % 2 == 0 or x % 3 == 0) {
		return false;
	}
	else {
		for (int i = 5; i * i <= x; i++) {
			if (x % i == 0 or x % (i + 2) == 0) {
				return false;
			}
		}
		return true;
	}

}

std::vector<int> nGob::sumVector(std::vector<int> a, std::vector<int> b) {
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

std::vector<int> nGob::toVector(unsigned int x) {
	unsigned int numDigits = trunc(log10(x)) + 1;
	std::vector<int> digits;
	for (int i = 0; i < numDigits; i++) {
		digits.push_back(x % 10);
		x = (x - (x % 10)) / 10;
	}
	return digits;
}