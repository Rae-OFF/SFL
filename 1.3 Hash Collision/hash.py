def hash_collision(string):
    if len(string) > 16:
        print("Input too long")
        return ""
    while len(string) < 16:
        string += "1"
    print('string: ', string)
    listOfChars = [char for char in string]
    print('listOfChars: ', listOfChars)
    listOfNumbers = [ord(char) for char in listOfChars]
    print('listOfNumbers: ', listOfNumbers)
    calc = 1
    for i in range(1, len(string) - 1, 1):
        calc += (listOfNumbers[i] * (i + 1))

        print('listOfNumbers[%s] * (%s + 1): ' % (i, i), listOfNumbers[i], '* ', '(%s + 1)'%i)
        print()
        print('calc: ', calc)
        print(listOfNumbers[i] * (i + 1))
        print('')


    print('calc1: ', calc)
    calc += listOfNumbers[0] * listOfNumbers[len(string) - 1]
    print(listOfNumbers[0] * listOfNumbers[len(string) - 1])
    print('calc2: ', calc)
    print('type of calc2: ', type(calc))
    stringResult = str(calc)
    print('type of str(calc2): ', type(stringResult))
    print('stringResult: ', stringResult)
    reverse = True
    temp = ""
    print(" -------- ")
    for char in stringResult:
        print('char in stringResult: ', char)
        if char != "9":
            temp += chr(ord(char) + 1)
            print('ord(char): ', ord(char), 'chr(ord(char)): ', chr(ord(char)))
            print('if char != "9", temp: ', temp)
            print(" -------- ")
        else:
            temp += chr(ord(char) - 1)
            print('else, temp: ', temp)
        print('original_stringResult: ', stringResult)
    while len(stringResult) < 16:
        if reverse:
            reverse = False
            stringResult += stringResult[::-1]
            print()
            print('reverse_stringResult: ', stringResult)
        else:
            stringResult += temp
            reverse = True
            print('1.else: not reverse: ', stringResult)
            print()
    last_16_chars = stringResult[-16:]
    print('last_16_chars: ', last_16_chars)


    finalResult = ""
    for i in range(0, len(last_16_chars), 4):
        finalResult += chr(int(last_16_chars[i] + last_16_chars[i + 1] + last_16_chars[i + 2] + last_16_chars[i + 3]))
        print('###')
        print('finalResult: ', finalResult)
        print('last_16_chars[%s]: ' % i, last_16_chars[i])
        print('last_16_chars[%s +1]: ' % i, last_16_chars[i + 1])
        print('last_16_chars[%s +2]: ' % i, last_16_chars[i + 2])
        print('last_16_chars[%s +3]: ' % i, last_16_chars[i + 3])
        print('int(): ', int(last_16_chars[i] + last_16_chars[i + 1] + last_16_chars[i + 2] + last_16_chars[i + 3]))
        print('###')
    return finalResult

if __name__ == '__main__':

    print(hash_collision('C0LLuSI0NM3sSaG3'))
    print()
    print(hash_collision('C0LLuSI0NN3sS\K3'))

    a = hash_collision('C0LLuSI0NM3sSaG3')
    b = hash_collision('C0LLuSI0NN3sS\K3')
    print(a == b)
