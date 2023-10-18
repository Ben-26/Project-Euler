#include <iostream>
#include <vector>

// https://github.com/stbrumme/euler/blob/master/euler-0026.cpp

unsigned int period(unsigned int x); // Returns the period length

int main(){
    std::vector<unsigned int> cache = { 0 }; 

    unsigned int d_max = 0;
    unsigned int p_max = 0; 
    for (unsigned int denominator = 1; denominator <= 1000; denominator++)
    {
        unsigned int length = period(denominator);
        if (p_max < length)
        {
            p_max = length;
            d_max = denominator;
        }
        cache.push_back(d_max);
    }
    std::cout << cache.at(cache.size() - 1);
    return 0;
}

unsigned int period(unsigned int x) {
    if (x == 0) {
        return 0;
    }

    const unsigned int NotSeenYet = 0;
    std::vector<unsigned int> lastPos(x, NotSeenYet);
    unsigned int position = 1;
    unsigned int q = 1; // Quotient

    while (true){
        unsigned int r = q % x; // remainder
        if (r == 0) {
            return 0;
        }
        if (lastPos[r] != NotSeenYet) {
            return position - lastPos[r];
        }
        lastPos[r] = position;
        position++;
        q = r * 10;
    }
}