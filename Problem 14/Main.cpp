#include <iostream>
#include <climits>

int hailstone(unsigned long long int i);

int main() {
	int chainMax = 0;
	int chainMaxValue = 0;
	for (unsigned long int i = 1; i < 1000000; i++) {
		int chain = hailstone(i);
		if (chain >= chainMax) {
			//std::cout << i << " chain: " << chain << std::endl;
			chainMax = chain;
			chainMaxValue = i;
		}
	}
	std::cout << chainMaxValue << " has the longest chain: " << hailstone(chainMaxValue) << std::endl;

	return 0;
}

int hailstone(unsigned long long int i) {
	int chain = 0;
	while (i > 1) {
		i = (i % 2 == 0 ? i / 2 : 3 * i + 1);
		chain++;
	}
	return chain;
}
