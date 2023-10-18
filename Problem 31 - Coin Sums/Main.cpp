#include <iostream>
#include <vector>

int main() {
	std::vector<unsigned int> coins = { 1, 2, 5, 10, 20, 50, 100, 200 };
	std::vector<unsigned int> cache(201, 0);
	cache.at(0) = 1;
	int subgroups;
	for (int i = 0; i < coins.size(); i++) {
		subgroups = coins.at(i);
		for (int j = subgroups; j <= 200; j++) {
			cache.at(j) += cache.at(j - subgroups);
		}
	}
	std::cout << cache.at(200);

	return 0;
}
 
/*
	value of coins := p
	number of subgroups:= s

	T(p, s) = 1 if d == 0				d = 0  corresponds to the 1p coin
			= T(p, s - 1) + T(p - denominations[s], s)			// Case exclusing the input coin + Cases including the input coin
			= T(p, s - 1) if p < denominations[s]

*/

