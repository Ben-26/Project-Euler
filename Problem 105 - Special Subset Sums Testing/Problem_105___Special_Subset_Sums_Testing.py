from itertools import combinations

def main():
    total = 0

    with open("0105_sets.txt", "r") as sets_file:
        for line in sets_file:
            A = [int(x) for x in line.rstrip().split(",")]
            
            subset_cache = []
            for i in range(1, len(A)):
                subset_cache += combinations(A, i)

            valid = True
            for i, B in enumerate(subset_cache):
                for C in subset_cache[i+1:]:
                    if set(B).isdisjoint(set(C)): 
                        sB = sum(B)
                        sC = sum(C)
                        
                        if sB == sC:
                            valid = False
                            break
                        
                        if (len(B) > len(C) and sB <= sC) or len(B) < len(C) and sB >= sC:
                            valid = False
                            break
                if not valid:
                    break
                
            if valid:  
                total += sum(A)

    print(total)
    
if __name__ == "__main__":
    main()