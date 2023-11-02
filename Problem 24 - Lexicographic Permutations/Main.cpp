#include <iostream>
#include <vector>

/*
 for limit = 999999: 2783915406
 for limit = 1000000: 2783915604

 skips the answer somehow 

ANS: 2783915460
*/
// 


int F(int x); // Factorial
std::vector<int> erase(std::vector<int> set, int removeIndex); // Removes the vector at the input index


int main() {
	std::vector<int> set = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }; // Current permutation
	std::vector<int> ans;
	int limit = 999999;
	int index;
	int size = set.size();
	for (int i = 0; i < size - 1; i++) {
		int f = F(set.size() - 1);
		index = trunc(limit / f);
		limit -= index * f;
		ans.push_back(set.at(index));
		set = erase(set, index);
	}
	ans.push_back(set.at(0));

	for (int i = 0; i < ans.size(); i++) {
		std::cout << ans.at(i);
	}

	return 0;
}

int F(int x) {
	if (x <= 2) {
		return 2;
	}
	else {
		return x * F(x - 1);
	}
}

std::vector<int> erase(std::vector<int> set, int removeIndex) {
	std::vector<int> r;
	for (int i = 0; i < set.size(); i++) {
		if (i != removeIndex) {
			r.push_back(set.at(i));
		}
		else {
			std::cout << "removing: " << set.at(i) << std::endl;
		}
	}
	return r;
}