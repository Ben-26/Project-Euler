n = 5000
pent_num = [0]*n

for k in range(1, n + 1):
    pent_num[k - 1] = int(0.5 * k * (3 * k - 1))
    
print(pent_num)

i = 0
j = 0
while not((pent_num[i] + pent_num[j] in pent_num) and (abs(pent_num[i] - pent_num[j]) in pent_num)):
    i += 1
    if i >= n - 1:
        i = 0
        j += 1
    if j >= n - 1:
        raise "Overflow"
        
print(f"{pent_num[i]}, {pent_num[j]}")
print(abs(pent_num[i] - pent_num[j]))