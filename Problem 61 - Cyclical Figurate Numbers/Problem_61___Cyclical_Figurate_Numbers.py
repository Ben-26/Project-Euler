"""
Generate all the 4 digit polygonal numbers
Append all the respective first and last digits to the respective start and end sets
Iterate through every polygonal number to see if
its start is in another end set and
its end is in another start set, if not; 
remove start and end, remove value itself

Repeat(?) - if a is linked to b and c and c gets removed, a no longer has a valid set
"""

def P(n, s):
    return ((s - 2) * n ** 2 - (s - 4) * n) // 2

def find_chain(polygonals, current_chain, visited, start):
    if len(current_chain) == 6:
        #if str(current_chain)[-2:] == str(start)[2:]:  broken??
        if current_chain[-1] % 100 == start // 100:
            return current_chain
        else:
            return None

    for p in range(3, 9):
        if not visited[p]:
            for val in polygonals[p]["start"].get(int(str(current_chain[-1])[-2:]), []):
                visited[p] = True
                result = find_chain(polygonals, current_chain + [val], visited, start)
                if result:
                    return result
                visited[p] = False
    
    return None

def main():
    bounds = [45, 140, 32, 100, 26, 81, 23, 70, 21, 63, 19, 58]
    polygonals = {}
    
    # Generate 4 digit polygonal numbers
    for i in range(3, 9):
        polygonals[i] = {"val" : [P(j, i) for j in range(bounds[2 * i - 6], bounds[2 * i - 5])],
                         "start" : {}, "end" : {}}
        polygonals[i]["val"] = [v for v in polygonals[i]["val"] if str(v)[2] != '0'] # Remove 3rd char 0s 
        for v in polygonals[i]["val"]:
            a = int(str(v)[:2])
            b = int(str(v)[-2:])
            polygonals[i]["start"].setdefault(a, set()).add(v)
            polygonals[i]["end"].setdefault(b, set()).add(v)

    # Remove values without a start and end in polygonals
    changed = False      
    while not changed:
        for i in range(3, 9):
            excl_set = [j for j in range(3, 9) if i != j]
            for v in polygonals[i]["val"]:
                a = int(str(v)[:2])
                b = int(str(v)[-2:])
                st = [j for j in excl_set if a in polygonals[j]["end"]]
                en = [j for j in excl_set if b in polygonals[j]["start"]]
                if (len(st) == 0 or len(en) == 0) or (len(st) == 1 and len(en) == 1 and st[0] == en[0]):
                    if a in polygonals[i]["start"]:
                        polygonals[i]["start"].pop(a)
                    if b in polygonals[i]["end"]:
                        polygonals[i]["end"].pop(b)
                    polygonals[i]["val"].remove(v)
                    changed = True

    # Generate chain
    for p in range(3, 9):
        for val in polygonals[p]["val"]:
            visited = {i: False for i in range(3, 9)}
            visited[p] = True
            chain = find_chain(polygonals, [val], visited, val)
            if chain:
                print(sum(chain))
                break
        if chain:
            break

if __name__ == "__main__":
    main()
   