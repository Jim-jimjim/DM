import statistics


w = 5


def partition(list, low, high):
    pivot = list[high]

    i = low - 1

    for j in range(low, high):
        if list[j] <= pivot:
            i += 1

            list[i], list[j] = list[j], list[i]

    (list[i + 1], list[high]) = (list[high], list[i + 1])

    return i + 1


def select_opt(list, k, left, right):
    while True:
        d = right - left + 1

        if d <= w:
            list[left:right] = sorted(list[left:right])
            result = left + k - 1
            return result

        dd = d // w

        for i in range(1, dd):
            list[left + (i - 1) * w:left + i * w - 1] = \
                sorted(list[left + (i - 1) * w:left + i * w - 1])

            list[left + i - 1], list[left + (i - 1) * w + w // 2 - 1] = \
                list[left + (i - 1) * w + w // 2 - 1], list[left + i - 1]

        v = select_opt(list, dd // 2, left, left + dd - 1)

        list[left], list[v] = list[v], list[left]

        v = partition(list, left, right - 1)

        temp = v - left + 1

        if k < temp:
            right = v - 1
        elif k == temp:
            result = v
            return result
        else:
            k -= temp
            left = v + 1


if __name__ == '__main__':
    l = [20, 12, 18, 16, 24, 10, 22, 14]
    print(l[select_opt(l, len(l) // 2, 0, len(l))])

    # для проверки
    print(statistics.median(l))
