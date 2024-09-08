"""
An addition chain is a finite sequence of integers (we call elements) 
1 = a0 < a1 < ... < ar = n with ai = aj + ak, i > j >= k >= 0 for a target n of length r

Research
https://oeis.org/A003313
https://wwwhomes.uni-bielefeld.de/achim/addition_chain.html
https://www-cs-faculty.stanford.edu/~knuth/programs/achain-all.w
http://additionchains.com/crouton.pdf
https://www.sciencedirect.com/science/article/pii/S0012365X20303861?ref=pdf_download&fr=RR-2&rr=8bf6d5f32b8e640c
"""

def main():
    l = [0] * 200 # Length of optimal chain 
    l[1] = 1
    
    a = [0] * 200 # Current generated chain
    b = [0] * 200 # Best chain 
    



if __name__ == "__main__":
    main()