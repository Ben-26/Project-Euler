
def reverseNumber(n):
   return int(str(n)[::-1]) 

def isPalindrome(n):
   return True if n == int(str(n)[::-1]) else False

def isLychrel(n):
   if n > 10**30: # Maximum - Should impliment 50 iterations rule
       return False
   else:
       n = n + int(str(n)[::-1])
       return True if n == int(str(n)[::-1]) else isLychrel(n)
     

if __name__ == "__main__":
   counter = 0
   for i in range(1, 10000):
         if not(isLychrel(i)):
            counter = counter + 1
   print(counter)
         
    