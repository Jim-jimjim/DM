from itertools import permutations


def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1

            array[i], array[j] = array[j], array[i]

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quick_sort(array, low, high, count):
    count += 1
    if low < high:
        count += 2
        pi = partition(array, low, high)

        count = quick_sort(array, low, pi - 1, count)

        count = quick_sort(array, pi + 1, high, count)
    return count


if __name__ == '__main__':
    with open("input.txt") as file:
        i = int(file.read())
    l = list(permutations(range(1, i + 1)))
    cc = []
    for i in range(0, len(l)):
        cc.append(quick_sort(list(l[i]), 0, len(list(l[i])) - 1, 0))

    maxx = max(cc)
    result = ''
    for i in range(0, len(l)):
        if maxx == cc[i]:
            print(l[i])
            result += str(l[i]) + '\n'

    with open("output.txt", 'w') as textFile1:
        textFile1.write(result)
