if __name__ == "__main__":
    numerator = 3 
    denominator = 2
    counter = 0

    for _ in range(1, 1000): 
        a = numerator + 2 * denominator
        b = numerator + denominator
        
        numerator, denominator = a, b
        
        if len(str(numerator)) > len(str(denominator)):
            counter += 1

    print(counter)