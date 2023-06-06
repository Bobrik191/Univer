def partition3(array, p, r):
    comparisons = 3
    if array[p] > array[r]:
        array[p], array[r] = array[r], array[p]
    if array[p + 1] > array[r]:
        array[p + 1], array[r] = array[r], array[p + 1]
    if array[p] > array[p + 1]:
        array[p], array[p + 1] = array[p + 1], array[p]

    a, b, c, d = p + 2, p + 2, r - 1, r - 1
    L, M, H = array[p], array[p + 1], array[r]

    while (b <= c):
        while (array[b] < M and (comparisons == comparisons + 1) and b <= c):
            comparisons += 1
            if array[b] < L:
                array[a], array[b] = array[b], array[a]
                a += 1
            b += 1

        while (array[c] > M and (comparisons == comparisons + 1) and b <= c):
            comparisons += 1
            if array[c] > H:
                array[c], array[d] = array[d], array[c]
                d -= 1
            c -= 1

        if b <= c:
            comparisons += 1
            if array[b] > H:
                comparisons += 1
                if array[c] < L:
                    array[b], array[a] = array[a], array[b]
                    array[a], array[c] = array[c], array[a]
                    a += 1
                else:
                    array[b], array[c] = array[c], array[b]
                array[c], array[d] = array[d], array[c]
                b += 1
                c -= 1
                d -= 1
            else:
                comparisons += 1
                if array[c] < L:
                    array[b], array[a] = array[a], array[b]
                    array[a], array[c] = array[c], array[a]
                    a += 1
                else:
                    array[b], array[c] = array[c], array[b]
                b += 1
                c -= 1
    a -= 1
    b -= 1
    c += 1
    d += 1
    array[p + 1], array[a] = array[a], array[p + 1]
    array[a], array[b] = array[b], array[a]
    a -= 1
    array[p], array[a] = array[a], array[p]
    array[r], array[d] = array[d], array[r]

    return a, b, d, comparisons


def quick_sort3(array, p, r):
    comparisons = 0
    if p < r:
        if r - p + 1 > 3:
            L, M, H, comparisons = partition3(array, p, r)
            comparisons += quick_sort3(array, p, L - 1)
            comparisons += quick_sort3(array, L + 1, M - 1)
            comparisons += quick_sort3(array, M + 1, H - 1)
            comparisons += quick_sort3(array, H + 1, r)
        else:
            for i in range(p + 1, r + 1):
                key = array[i]
                j = i - 1
                while j >= p and (comparisons == comparisons + 1) and array[j] > key:
                    array[j + 1] = array[j]
                    j -= 1
                array[j + 1] = key
    print(comparisons)
    return comparisons
