import numpy as np


# listOfNumbers:  [67, 48, 76, 76, 117, 83, 73, 48, 78, 77, 51, 115, 83, 97, 71, 51]
# 9522
# listOfNumbers:  [67, 65, 82, 76, 80, 72, 71, 65, 89, 90, 89, 82, 76, 90, 72, 51]

# if __name__ == '__main__' :

def find_array():
    arr1 = np.array([i for i in range(2, 16)])
    print(arr1)
    arr2 = np.array([48, 76, 76, 117, 83, 73, 48, 78, 77, 51, 115, 83, 97, 1])
    new_arr = np.multiply(arr2, arr1)

    sum = np.sum(new_arr)

    rel_arr = []
    # i = 15
    j = 2
    all = 9522
    print()
    print('arr222222: ', arr2)
    print('#####')
    while len(arr1)>1:
        num = all - sum
        print('%s = %s - %s' % (num,all,sum))
        rel_arr.append(np.ceil(num / arr1[-1]))
        arr2 = arr2[:len(arr2) - 1]
        arr2[len(arr2)-1] = 1
        print('arr2, ' , arr2)
        j = j+1
        all = all - (rel_arr[-1] * arr1[-1])
        arr1 = arr1[:len(arr1)-1]
        print('arr1, ', arr1)
        sum = np.sum(np.multiply(arr2, arr1))
        print('rel_arr, ', rel_arr)
        print('rel_arr[-1]: ', rel_arr[-1])
        print('all: ', all)
        print('sum, ', sum)
        print('#####')
    last_one = np.ceil((all - sum)/arr1[-1])
    rel_arr.append(last_one)
    rel_arr.reverse()
    int_rel_arr = np.array(rel_arr).astype(int)
    print(int_rel_arr)
    return int_rel_arr


def find_char(arr):
    list = []
    for x in arr:
        list.append(chr(x))
    print(list)
    return list


def code(string):
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
    return calc


rel_char = find_char(find_array())
null_str = ""
str = "C"+null_str.join(rel_char)+"3"
print('+++++++++++++++')
print(str)
print('+++++++++++++++')
print('result of String:', code(str))
