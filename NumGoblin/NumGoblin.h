#pragma once
#ifndef NUMGOBLIN_H
#define NUMGOBLIN_H

#include <vector>

class nGob {
public:
//	Functions ( Vector Adders, Factorial ) 
	unsigned int intFactorial(unsigned int x);

//	Algorithms ( Permutations, Search, Sort )
	bool palindrome(std::vector<int> digits);
	std::vector <std::vector<int>> pAlg(std::vector <std::vector<int>> S); 
	bool prime(int x);
	std::vector<int> sumVector(std::vector<int> A, std::vector<int> B);
	std::vector<int> toVector(unsigned int x);
	
};

#endif 