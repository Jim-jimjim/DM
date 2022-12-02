from numpy import loadtxt


def insertion_sort(array):
    count = 0
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        count += 1
        while (j >= 0) and (array[j] > temp):
            count += 1
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    return count


def shaker_sort(array):
    count = 0
    left = 0
    right = len(array) - 1

    while left <= right:
        for i in range(left, right, +1):
            count += 1
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
        right -= 1

        for i in range(right, left, -1):
            count += 1
            if array[i - 1] > array[i]:
                temp = array[i]
                array[i] = array[i - 1]
                array[i - 1] = temp
        left += 1
    return count


if __name__ == '__main__':

    # ============ 12.23 ============

    array1 = loadtxt('input1.txt', dtype='int')

    count = insertion_sort(array1)

    with open("output1.txt", 'w') as textFile1:
        textFile1.write(str(array1) + '\n')
        textFile1.write(str(count))

    # ============ 12.28 ============

    array2 = loadtxt('input1.txt', dtype='int')

    count = shaker_sort(array2)

    with open("output2.txt", 'w') as textFile1:
        textFile1.write(str(array2) + '\n')
        textFile1.write(str(count))
