def digitSum(n):
    return sum(map(int, str(n)))

if __name__ == "__main__":
    maxSum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            d_sum = digitSum(a**b)
            if maxSum < d_sum:
                maxSum = d_sum
    print(maxSum)