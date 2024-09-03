from math import sqrt

def main():
    for i in range(0, 10):
        num = int("".join([char + str(i) for char in "1234567890"])[:-1]) # Not a unique digit
        print(f"root {num} = {sqrt(num)}")
        if int(sqrt(num))**2 == num:
            print("sol = ", num)
            
if __name__ == "__main__":
    main()