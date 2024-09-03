def main():
    cubes = {}
    min_cube = float("inf")

    for i in range(10**5):
        cube_str = "".join(sorted(list(str(i**3))))
        cubes.setdefault(cube_str, []).append(i**3)

    for c in cubes:
        if len(cubes[c]) == 5:
            if min(cubes[c]) < min_cube:
                min_cube = min(cubes[c])
    print(min_cube)
                
if __name__ == "__main__":
    main()