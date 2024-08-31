def decrypt(cipher, a, b, c):
    decrypted = ''
    key = [a, b, c]
    
    for i in range(len(cipher)):
        decrypted += chr(key[i % 3] ^ cipher[i])
    return decrypted

def main():
    with open("0059_cipher.txt", "r") as cipher_file:
        cipher = [int(char) for char in cipher_file.readline().rstrip().split(",")]   

    possibly_coherent = []

    for a in range(97, 123):
        for b in range(97, 123):
            for c in range(97, 123):
                decrypted_str = decrypt(cipher, a, b, c)
                if "the" in decrypted_str and "and" in decrypted_str: # Running once gives us the possible candidates and we see its the 6th str
                    possibly_coherent.append(decrypted_str)
                    #print(decrypted_str)
    
    counter = 0
    for char in possibly_coherent[5]:
        counter += ord(char)

    print(counter)
    

if __name__ == "__main__":
    main()
