#include <iostream>
#include <vector>

int main() {
	std::vector<int> digits = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };

	return 0;
}
// assign each variable to either multiplicand, multiplier or product set
// {a} x {b} = {c} with {a} and {b} being assigned and c being the remainder
// permutate each set and compute equivalence
// cache product 

/*
In {{{}}, {1, 2, ... , n}}
Return {{{1}}, {2, ... , n}}

In {{1}, {2, ... , n}}
Return {{{1, 2}, {2, 1}}, {3 , ... , n}}

In {{{1, 2}, {2, 1}}, {3 , ... , n}} 
Return {{{1, 2, 3}, ... , {2, 1, 3}}, {4 , ... , n}}

... 

In {{{1, ... , n} , ... , {n , ... , 1}}, {{}}}

-----------------------------------------------------------------------------
Pseudocode:
In {A := {{}}, B:= {1, 2, ... , n}}
K := A.size
N := B.size 

for(i = 0 to (K - 1)!)
	# want to iterate over every set in A
	for(j = 0 to N
	need inverse factorial as we are given a set of k items s.t. n! = k, need to then iterate over each set k n times

	A.at(i).at(j)

Notes:
num subsets in A = (n - k)!
when taking B[0] could order the list backwards and pop back 
order doesnt matter so could just pop as normal 

Worked example

for {{}} {1, ... , n}
K := 1
N := n
for i = 0 ; i < (K-1)!
	take B[0] 
	for j = 0 to K
		return set += {1}
	end for

iterator for set in A and item from B
Example																Generalising
IN {{{1, 2}, {2, 1}}, {3, 4, ... , n}}								In {A := {{...}, {...}} , B := {... , n - 1, n}} A is the permutated subsets, B is elements left to permutate
K := 2																K := Size of A ( number of sets it contains ) 
N := n - 2															N := n - K / size of B <- More general 
take 3 from {3, 4, ... , n}}										take B_0 from B <- This is the next element that will be "added" to the permutations
i E {0, 1}															i in 0 to K-1 <- i is for sets 
need to insert 3 in (K+1)! places									j in 0 to (K+1)! - 1 is for the position in the set A_i where the element B_0 should be placed 
0 1 2 in {}i = 0													i = j = 0
0 1 2 in {}i = 1													while i < K - 1
																		create new empty set
j mod 3 with j E {0, ..., 5}											if j mod (K+1) = 0 incrimiment i
remove B_0 from B														if i = j, empty set push back B_0
																		else empty set push back A_0_j
Return {{{1, 2, 3}, {1, 3, 2,}, ...} , {4, 5, ... , n}}
*/
