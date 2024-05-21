def prev_perm(a):
    n = len(a)
    i = n - 2
    while i >= 0 and a[i] <= a[i + 1]:
        i -= 1
    if i < 0:
        return a[:-1][::-1] if n > 1 else [1]
    k = n - 1
    while a[i] <= a[k]:
        k -= 1
    a[i], a[k] = a[k], a[i] # swap
    a[i + 1:] = a[i + 1:][::-1] # [::-1] reverses list
    return a

def prime(x):
    if (x == 2):
        return True
    if (x < 2 or x % 2 == 0):
        return False
        
    i = 3
    while (i*i < x):
        if(x % i == 0):
            return False
        i+=2
    return True

n = 10

x = [i for i in range(1, n)]

while not(prime(int(''.join(map(str, x))))): 
    if x == [1]:
        break
    x = prev_perm(x)

print(f"Prime: {''.join(map(str, x))}")