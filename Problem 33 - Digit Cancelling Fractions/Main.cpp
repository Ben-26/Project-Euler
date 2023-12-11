#include <iostream>
#include <vector>

int gcd(int x, int y);
bool commonDigit(int x, int y);
float digitRemovedFraction(int x, int y);


int main() {
	std::vector<std::vector<int>> fraction; // {Numerator, Denominator} 


	//std::cout << digitRemovedFraction(49, 98);


	
	for (int i = 10; i < 100; i++) {
		for (int j = 10; j < 100; j++) {
			int g = gcd(i, j);
			if (g != 1 && g % 10 != 0) {
				if (commonDigit(i, j)) {
					if ((float)i / j == digitRemovedFraction(i, j) && (float)i / j < 1) {
						fraction.push_back({ i, j });
					}
				}
			}
		}
	}

	for (int i = 0; i < fraction.size(); i++) {
		std::cout << fraction.at(i).at(0) << "/" << fraction.at(i).at(1) << "\n";
	}

	return 0;
}

int gcd(int x, int y){
	int a = x > y ? x : y;
	int b = x > y ? y : x;
	return (b == 0) ? a : gcd(b, a % b);
}

bool commonDigit(int x, int y) {
	if ((x % 10 == y % 10) || ((x / 10) % 10 == y % 10) || (x % 10 == (y / 10) % 10) || ((x / 10) % 10 == (y / 10) % 10)) {
		return true;
	} 
	return false;
}

float digitRemovedFraction(int x, int y) {
	if (x % 10 == y % 10) { //								an / bn 
		//std::cout << "1";
		return (float)((x / 10) % 10) / (y / 10 % 10);
	}
	else if ((x / 10) % 10 == y % 10) { //					na / bn
		//std::cout << "2";
		return (float)(x % 10) / (y / 10 % 10);
	}
	else if (x % 10 == (y / 10) % 10) { //					an / nb
		//std::cout << "3";
		//std::cout << (x / 10) % 10 << " , " << y % 10 << "\n";
		return (float)((x / 10) % 10) / (y % 10);
	}
	else {//												na / nb
		//std::cout << "4";
		return (float)(x % 10) / (y % 10);
	}
}

