
def is_valid(x1, y1, x2, y2):
    if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0):
        return False
    if (x1 == 0 and x2 == 0) or (y1 == 0 and y2 == 0):
        return False
    
    if (x1 == x2 and y1 == y2):
        return False

    x = x1**2 + y1**2
    y = x2**2 + y2**2
    z = (x1 - x2)**2 + (y1 - y2)**2
    
    return x + y == z or x + z == y or y + z == x


def main():
    N = 50
    counter = 0
    for x2 in range(1, N + 1):
        for y1 in range(1, N + 1):
            for x1 in range(x2 + 1):
                for y2 in range(y1 + 1):
                    counter += is_valid(x1, y1, x2, y2)
    print(counter)

if __name__ == "__main__":
    main()
    