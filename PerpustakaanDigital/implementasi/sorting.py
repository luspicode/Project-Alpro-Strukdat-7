def bubble_sort_judul(data):
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j]['judul'].lower() > data[j + 1]['judul'].lower():
                data[j], data[j + 1] = data[j + 1], data[j]
