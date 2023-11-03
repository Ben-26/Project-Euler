#include <iostream>
#include <vector>

std::vector<std::vector<int>> pAlg(std::vector<std::vector<int>> A, std::vector<int> B); // Permutations algorithm - See Analysis.txt
unsigned int factorial(unsigned int x); // Returns x!

int main() {
	std::vector<int> digits = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	
	std::vector<int> test = { 1, 2, 3 };
	std::vector < std::vector<int>> temp = pAlg({ {} }, test);
	for (int i = 0; i < temp.size(); i++) {
		for (int j = 0; j < temp.at(i).size(); j++) {
			std::cout << temp.at(i).at(j) << " ";
		}
		std::cout << "\n";
	}

	return 0;
}

unsigned int factorial(unsigned int x) {
	return x > 1 ? x * factorial(x - 1) : (x == 0 or x == 1 ? 1 : 0);
}

std::vector<std::vector<int>> pAlg(std::vector<std::vector<int>> A, std::vector<int> B) {
	int X = A.size(); // Number of subsets in A
	int Y = A.at(0).size(); // Size of the subsets in A
	int elements = B.size(); // Number of elements in B
	if (elements == 0) {
		return A;
	}
	else {
		int Z = B.at(elements - 1); // element to move into the new sets
		std::vector < std::vector<int>> pSet; // set of new permutations 

		// creating the new sets
		for (unsigned int i = 0; i < factorial(X + 1) - 1; i++) {
			std::vector<int> subset; // will be filled to a size of n+1 
			for (unsigned int j = 0; j < X; j++) { // Selects current set from A
				
			}

			unsigned int j = 0;
			while (j < X + 1) {
				if (i % (X + 1) == j) {

				}
				j++;
			}
		}

		/*
		for N = 2
		example sets {1, 2} and {2, 1} with k = 3
		i = 0, 1, 2, 3, 4, 5
		i % 3 = 0, 1, 2, 0, 1, 2
		take elements 0, 1 from {1, 2} then
		place element at = i % 3 
		j = iterate through subset
		*/
		B.pop_back();
		return pAlg(pSet, B);
	}
}
/*
Generalising

permutations In {A := {{...}, {...}} , B := {... , n - 1, n}} A is the permutated subsets, B is elements left to permutate
K := Size of A ( number of sets it contains )
N := n - K / size of B <- More general
If N = 0 
	return A
Else 
	take B_0 from B <- This is the next element that will be "added" to the permutations
	i in 0 to K-1 <- i is for sets 
	j in 0 to (K+1)! - 1 is for the position in the set A_i where the element B_0 should be placed
	i and j wrong way round **********
	i = j = 0
	while i < K - 1
		create new empty set
		if j mod (K+1) = 0 incrimiment i
		if i = j, empty set push back B_0
		else empty set push back A_0_j // check index
	remove the element B_0 that was "added"
	return permutations {{new permutations sets}, B \ B_0}

	// remake iterator 
		// i is index over the sets i E {1, ... , k}
		// j is index over each subset j E {1, ... , A.at0
*/

