#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

std::vector<std::vector<int>> read_triangle(const std::string& filename) {
    std::ifstream file(filename);
    std::vector<std::vector<int>> triangle;
    std::string line;

    while (std::getline(file, line)) {
        std::istringstream iss(line);
        std::vector<int> row;
        int number;
        while (iss >> number) {
            row.push_back(number);
        }
        triangle.push_back(row);
    }

    return triangle;
}

int maximum_total(std::vector<std::vector<int>>& triangle) {
    int n = triangle.size();
    // Start from the second last row and move upwards
    for (int i = n - 2; i >= 0; --i) {
        for (int j = 0; j < triangle[i].size(); ++j) {
            triangle[i][j] += std::max(triangle[i + 1][j], triangle[i + 1][j + 1]);
        }
    }
    // The top element now contains the maximum total
    return triangle[0][0];
}

int main() {
    std::string filename = "triangle.txt";
    std::vector<std::vector<int>> triangle = read_triangle(filename);
    int max_total = maximum_total(triangle);
    std::cout << "Maximum total from top to bottom is " << max_total << std::endl;
    return 0;
}
