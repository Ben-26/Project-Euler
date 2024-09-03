
def main():
    cache = {}
    with open("0079_keylog.txt", "r") as keylog_file:
        for line in keylog_file:
            key = list(line.strip())
            cache.setdefault(key[0], set()).update([key[1], key[2]])
            cache.setdefault(key[1], set()).add(key[2])

    sorted_keys = sorted(cache.keys(), key=lambda k: len(cache[k]))   
    password = ""
    for i in range(len(sorted_keys) - 1, -1, -1):
        password += str(sorted_keys[i])
        
    print(password + "0") # 9 in the dict points to 0

if __name__ == "__main__":
    main()