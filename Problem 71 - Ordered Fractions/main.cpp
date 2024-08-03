#include <iostream>

int main() {
    int best_numerator = 0;
    int best_denominator = 1;
    for (int d = 1; d < 1000000; d++) {
        int n = (3 * d) / 7; // 3/7 = n/d -> 3d / 7 = n
        if (7 * n != 3 * d) {
            if ((3 * best_denominator - 7 * best_numerator) * d > (3 * d - 7 * n) * best_denominator) {
                best_numerator = n;
                best_denominator = d;
            }
        }
    }
    std::cout << best_numerator;
    return 0;
}