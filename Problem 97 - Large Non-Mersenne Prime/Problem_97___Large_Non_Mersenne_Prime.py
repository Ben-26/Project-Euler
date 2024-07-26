def main():
    last_ten_digits = 1
    for i in range(7830457):
        last_ten_digits = (last_ten_digits * 2) % 10**10
    
    print((28433 * last_ten_digits % 10**10) + 1)

if __name__ == "__main__":
    main()
