def bubble_sort_judul(data):
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j]['judul'].lower() > data[j + 1]['judul'].lower():
                data[j], data[j + 1] = data[j + 1], data[j]


def quick_sort_judul(data, low, high):
    if low < high:
        pi = partition(data, low, high)

        quick_sort_judul(data, low, pi - 1)
        quick_sort_judul(data, pi + 1, high)


def partition(data, low, high):
    pivot = data[high]['judul'].lower()
    i = low - 1

    for j in range(low, high):
        if data[j]['judul'].lower() < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1


def merge_sort_judul(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sort_judul(left)
        merge_sort_judul(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i]['judul'].lower() < right[j]['judul'].lower():
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
