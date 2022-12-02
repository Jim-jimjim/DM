import math

from numpy import loadtxt


def shell_sort2(array):
    count = 0
    h = 1
    while h < math.log2(len(array)):
        h = h * 2 + 1
    while h > 0:
        print(h)
        for i in range(h, len(array), 1):
            tmp = array[i]
            inner = i
            while (inner > h - 1) and (array[inner - h] > tmp):
                count += 1
                array[inner] = array[inner - h]
                inner -= h
            array[inner] = tmp
        h = (h - 1) // 2
    return array, count


def shell_sort3(array):
    count = 0
    h = 1
    while h < math.log(2 * len(array) + 1, 3) - 1:
        h = h * 3 + 1
    while h > 0:
        print(h)
        for i in range(h, len(array), 1):
            tmp = array[i]
            inner = i
            while (inner > h - 1) and (array[inner - h] > tmp):
                count += 1
                array[inner] = array[inner - h]
                inner -= h
            array[inner] = tmp
        h = (h - 1) // 3
    return array, count


if __name__ == '__main__':
    # ============ 12.43 1 ============

    array1 = loadtxt('input.txt', dtype='int')

    array1, count1 = shell_sort2(array1)

    with open("output1.txt", 'w') as textFile1:
        textFile1.write(str(array1) + '\n')
        textFile1.write(str(count1))

    print("====================")

    # ============ 12.43 2 ============

    array2 = loadtxt('input.txt', dtype='int')

    array2, count2 = shell_sort3(array2)

    with open("output2.txt", 'w') as textFile1:
        textFile1.write(str(array2) + '\n')
        textFile1.write(str(count2))
