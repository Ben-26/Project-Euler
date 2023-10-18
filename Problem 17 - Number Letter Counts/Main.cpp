#include <iostream>
#include <cmath>
#include <vector>


int f(int n); // Returns the number of letters in a number 
int index(int n); // Holds all the number word totals

int main() {
	long long total = 0;
	for(int i = 1; i <= 1000; i++){
		//std::cout << i << ": " << f(i) << std::endl;
		total += f(i);
	}
	std::cout << total;
	return 0;
}

int f(int n) {
	// n = abc
	// Split digits into vector {a, b, c}
	// If a > 0 -> If b > 1 -> If b & c = 0
	std::vector<int> v;
	int d = trunc(log10(n)) + 1; // Number of digits 
	for (int i = d; i > 0; i--) {
		v.push_back(trunc(n / pow(10, i - 1)));
		n -= v.at(d - i) * pow(10, i - 1);
	}
	if (v.size() == 4) { // 4 Digit number 
		return index(v.at(0)) + index(1000);
	}
	else {
		if (v.size() == 3) { // 3 Digit number 
			if (v.at(1) > 1) { // 10b + c !E [1, 19]
				return index(v.at(0)) + index(100) + index(10 * v.at(1)) + 3 + index(v.at(2)); // a + 100 + 10b + 'and' + c
			}
			else {
				if ((v.at(1) == 0) && (v.at(2) == 0)) { // Dont include +3 for 'and' 
					return index(v.at(0)) + index(100); // a + 100
				}
				else {
					return index(v.at(0)) + index(100) + 3 + index(10 * v.at(1) + v.at(2)); // a + 100 + 'and' + (10b+c)
				}

			}
		}
		else {
			if (v.size() == 2) { // 2 Digit number 
				if (v.at(0) > 1) {
					return index(10 * v.at(0)) + index(v.at(1)); // [20, 99]
				}
				else {
					return index(10 * v.at(0) + v.at(1)); // [1, 19]
				}

			}
			else {
				if(v.size() == 1) { // 1 Digit number
					return index(v.at(0));
				}
				else {
					std::cout << "AAAAAAAAAAAAAAAAAAAAAAA";
				}
			}
		}
	}




}

int index(int n) {
	if (n == 0) {
		return 0;
	}
	if (((n == 1) || (n == 2)) || ((n == 6) || (n == 10))) {
		return 3;
	}
	if (((n == 4) || (n == 5)) || (n == 9)) {
		return 4;
	}
	if ((((n == 3) || (n == 7)) || ((n == 8) || (n == 50))) || (n == 60) || (n == 40)) {
		return 5;
	}
	if ((((n == 11) || (n == 12)) || (n == 20)) || (((n == 30) || (n == 80) || (n == 90)))) {
		return 6;
	}
	if (((n == 15) || (n == 70)) || ((n == 100) || (n == 16))) {
		return 7; 
	}
	if ((((n == 13) || (n == 14)) || ((n == 18) || (n == 19))) || (n == 1000)) {
		return 8;
	}
	if (n == 17) {
		return 9;
	}
}


/*
Separate components -> Hundreds & 10s, if [20, 99] separate 10s
Lexical structure, of a*100 + b*10 + c*1
case 1: b*10 + c E [1, 19]
	a hundred and <b*10+c>;
case 2: b*10 + c E [20, 99]
	a hundred and <b*10> - <c> 


INDEX

Number | Word | Sum
1, One, 3 
2, Two, 3
3, Three, 5
4, Four , 4
5, Five, 4
6, Six, 3
7, Seven, 5
8, Eight, 5
9, Nine, 4
10, Ten, 3

11, Eleven, 6
12, Twelve, 6
13, Thirteen, 8
14, Fourteen, 8
15, Fifteen, 7
16, Sixteen,7
17, Seventeen, 9
18, Eighteen, 8
19, Nineteen, 8

20, Twenty, 6
30, Thirty, 6
40, Fourty, 6
50, Fifty, 5
60, Sixty, 5
70, Seventy, 7
80, Eighty, 6
90, Ninety, 6

x00, hundred, 7
x000, thousand, 8
- , and, 3

*/