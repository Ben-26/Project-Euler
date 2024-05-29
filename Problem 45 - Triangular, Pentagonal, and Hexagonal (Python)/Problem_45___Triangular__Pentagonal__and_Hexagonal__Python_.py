from math import sqrt

n = 285
found = False

while not(found):
    n += 1
    P = sqrt(12 * n * (n + 1) + 1)
    H = sqrt(4 * n * (n + 1) + 1)
    if (P % 6 == 5 and H % 4 == 3):
        found = True

print(n * (n + 1) / 2)