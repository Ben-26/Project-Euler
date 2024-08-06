
def main():
    cache = [0] * 101
    cache[0] = 1

    for i in range(1, 101):
        for j in range(i, 101):
            cache[j] += cache[j - i]
    
    # All values in cache are 1 greater than intended 
    #for i in range(1, 101):
    #    cache[i] -= 1 
        
    print(cache[-1] - 1)

if __name__ == "__main__":
    main()
