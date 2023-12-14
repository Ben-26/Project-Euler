#include <iostream>
#include <cmath>

int main() {
	int n = 1;
	unsigned int prod = 1;
	unsigned int i = 2;
	unsigned int digits = 2;
	while (digits <= 1000000) {
		i++;
		if (digits + trunc(log10(i)) + 1 >= pow(10, n)) {
			std::cout << "over " << pow(10, n) << " digits\n";
			std::cout << "concatenating: " << i << " number has " << digits << " digits\n";
			n++;
			//note: used the values of i and d to manually calculate the 10^n'th value 
		}
		digits += trunc(log10(i)) + 1;
	}
	std::cout << prod;

	return 0;
}

/*
Useless analysis: 
want d(1 10 100 1000 10000 100000 1000000)



n		range ( 10^(n-1) - 10^n)	numbers	in this range	digits of the constant								
1		1-9							9						1-9								d1

2		10-99						89						10-188							d10 d100
3		100-999						899						189-1987						d1000
4		1000-9999					8999					1988-19986						d10000
5		10000-99999					89999					19987-199985					d100000
6		100000-999999				899999					199986-1999984					d1000000


1+1+1+1+...+1 + 2 + 2 + 2 + 2 + 

from d_1 to d_10 -> 9 incriments of 1 -> first 9 1 digit numbers -> 1 + 9 = 10 

from d_10 to d_100 -> 45 incriments of 2 -> first 45 2 digit numbers -> 10(1 digit) + 44(2 digit) = 54

from d_100 to d_1000 -> 300 incriments of 3 -> first 300 3 digit numbers -> 44*2 = 399 

...

from d_10^n to d_10^(n+1) -> 9*10^n / (n+1) incriments of n+1 -> first 9*10^n / (n+1)  n+1 digit numbers -> 10^n + 9*10^n / (n+1) - 1  = 10^n(n+10)/(n+1) - 1
																												

we have for nEN a_n = 9*10^n - 1 where a_n is the number of numbers with n digits, i.e. there are 89 2 digit numbers
we want the 10^n'th digit , 


Range: 2*10^n - (n + 10) to 2*10^(n + 1) - (n + 11) add incriments of n  

*/