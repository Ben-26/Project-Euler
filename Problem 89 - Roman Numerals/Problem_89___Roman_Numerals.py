def main():
    roman_vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_chars = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    saved = 0

    with open("0089_roman.txt", "r") as roman_file:
        for numeral in roman_file:
            numeral = numeral.rstrip()
            min_roman = numeral    
            
            numeral_val = 0
            for char in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                if char in min_roman:
                    numeral_val += roman_vals[roman_chars.index(char)]
                    min_roman = min_roman.replace(char, "")

            for char in min_roman:
                numeral_val += roman_vals[roman_chars.index(char)]
                min_roman = min_roman.replace(char, "")

            # Converting numeral_val to numerals 
            i = 0
            while numeral_val > 0:
                for _ in range(numeral_val // roman_vals[i]):
                    min_roman += roman_chars[i]
                    numeral_val -= roman_vals[i]
                i += 1
            saved += (len(numeral) - len(min_roman))
    print(saved)

if __name__ == "__main__":
    main()
