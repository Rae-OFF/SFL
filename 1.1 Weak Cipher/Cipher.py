def readFileContent(file_path):
    file = open(file_path, "r")
    content = file.read()
    return content

# Read the encrypted string from the file
filePath = "encryptedXor.txt"
encryptedText = readFileContent(filePath)
print(f"Encrypted Text: {encryptedText}")

def funk():
    for dec in range(255):
        key = int(bin(dec), 2)
        # print(key)
        for char1 in encryptedText:
            char2 = int(ord(char1))
            # print(char2)

            ans = char2 ^ key
            print(chr(ans), end="")
        print(f"\t{dec}", end="")
        print()

funk()