"""
https://totologic.blogspot.com/2014/01/accurate-point-in-triangle-test.html
Method 1
"""

def main():
    c = []
    counter = 0
    with open("0102_triangles.txt") as coordinates_file:
        for coords in coordinates_file:
            c = [int(char) for char in coords.rstrip().rsplit(",")]
            # [x1, y1, x2, y2, x3, y3]
            denom = (c[3] - c[5])*(c[0] - c[4]) + (c[4] - c[2])*(c[1] - c[5])
            a = ((c[3] - c[5])*-c[4] + (c[4] - c[2])*- c[5]) / denom
            b = ((c[5] - c[1])*-c[4] + (c[0] - c[4])*- c[5]) / denom
            c = 1 - a - b
            
            counter += int(0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1)
    print(counter)             
 

if __name__ == "__main__":
    main()
