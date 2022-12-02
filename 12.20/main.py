from numpy import loadtxt


def p_search(array, target):
    for i in range(0, len(array)):
        if target == array[i]:
            return i
    return 0


def b_search(array, target):
    low = 0
    high = len(array) - 1
    count = 0

    while low <= high:
        mid = (high + low) // 2
        count += 1

        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            return count

    return count


def i_search(array, low, high, target, count):
    count += 1
    if low <= high and array[low] <= target <= array[high]:

        pos = low + ((high - low) // (array[high] - array[low]) *
                     (target - array[low]))

        if array[pos] < target:
            return i_search(array, pos + 1, high, target, count)
        elif array[pos] > target:
            return i_search(array, low, pos - 1, target, count)
        else:
            return count
    return count


if __name__ == '__main__':

    # ============ 12.20 1 ============

    array1 = loadtxt('input1.txt', dtype='int')

    count = 0
    for i in range(1, len(array1) + 1):
        count += p_search(array1, i) + 1

    with open("output1.txt", 'w') as textFile1:
        textFile1.write(str(count / len(array1)))

    # ============ 12.20 2 ============

    array2 = loadtxt('input2.txt', dtype='int')

    count = 0
    for i in range(1, len(array2) + 1):
        count += b_search(array2, i)

    with open("output2.txt", 'w') as textFile1:
        textFile1.write(str(count / len(array2)))

    # ============ 12.20 3 ============

    array3 = loadtxt('input3.txt', dtype='int')

    count = 0
    for i in range(1, len(array3) + 1):
        count += i_search(array3, 0, len(array3) - 1, i, 0)

    with open("output3.txt", 'w') as textFile1:
        textFile1.write(str(count / len(array3)))
