tri_num = [0]*1001
total = 0

for i in range(0, 1000):
    tri_num[i] = 0.5 * i * (i + 1)

word_str = open("0042_words.txt", "r").readline().replace('"', '').rsplit(",")
for word in word_str:
    x = 0
    for char in word:
        x += ord(char) - 64
    if x in tri_num:
        total += 1

print(total)