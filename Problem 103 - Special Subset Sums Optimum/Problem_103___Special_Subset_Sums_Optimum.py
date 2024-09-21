from itertools import combinations # succumbed to library use


def main():
    lb = 20
    ub = 47
    
    min_sum = float('inf')
    optimum = []

    for k in range(ub - lb - 1):
        for a1 in range(lb + 1, ub - 4 - k):
            for a2 in range(a1 + 1, ub - 3 - k):
                for a3 in range(a2 + 1, ub - 2 - k):
                    for a4 in range(a3 + 1, ub - 1 - k):
                        for a5 in range(a4 + 1, ub - k):
                            A = [lb, a1, a2, a3, a4, a5, ub - k]
                            subset_cache = []
                            for i in range(1, len(A)):
                                subset_cache += combinations(A, i)

                            valid = True 
                            for i, B in enumerate(subset_cache):
                                for C in subset_cache[i+1:]:
                                    if set(B).isdisjoint(set(C)):
                                        sB = sum(B)
                                        sC = sum(C)
                                        if sB == sC or (len(B) > len(C) and sB < sC):
                                            valid = False
                                            break
                                if not valid:
                                    break
                        
                            if valid and sum(A) <= min_sum:
                                min_sum = sum(A)
                                optimum = A
                       
                            if valid:
                               # 20313839404245 from observing outputs here
                               print("".join(str(a) for a in A) + " is valid with sum = ", sum(A))     
        print("Lowering k")                         
                                 
    print("Final result = " + "".join(str(v) for v in sorted(optimum)))
                           
if __name__ == "__main__":
    main()