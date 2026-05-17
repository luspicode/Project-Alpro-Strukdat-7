class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("antrian kosong")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("antrian kosong")

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

#tes semua fungsi
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue("Buku A")
    queue.enqueue("Buku B")
    queue.enqueue("Buku C")
    print(queue)  # Output: ['Buku A', 'Buku B', 'Buku C']
    print(queue.dequeue())  # Output: 'Buku A'
    print(queue.peek())  # Output: 'Buku B'
    print(queue.size())  # Output: 2
    queue.clear()
    print(queue.is_empty())  # Output: True