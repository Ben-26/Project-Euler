def isSameDigits(a, b):
    return True if set(a).issubset(set(b)) else False


if __name__ == "__main__": 
    found = False
    i = 1
    while not(found):
        if sorted(str(2 * i)) == sorted(str(3 * i)) and sorted(str(2 * i)) == sorted(str(4 * i)) and sorted(str(2 * i)) == sorted(str(5 * i)) and sorted(str(2 * i)) == sorted(str(6 * i)):
            found = True
            print(i)
        else:
            i = i + 1
