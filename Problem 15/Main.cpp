#include <iostream>
#include <vector>


int main() {
	const int n = 4; // Grid dimensions
	std::vector<int> grid;
	
    for (int i = 0; i < 2 * n; i++) {
		if (i % 2 == 0) {
			grid.push_back(0); 
		}
		else {
			grid.push_back(1);
		}
	}

	// Merge sort method 
	// https://en.wikipedia.org/wiki/Steinhaus%E2%80%93Johnson%E2%80%93Trotter_algorithm
	

	// Used (2n!) / (n!)^2 where n = grid dimension 


	return 0;
}

