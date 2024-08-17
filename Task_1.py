import heapq

def heap_sort(iterable):
    heap = list(iterable)
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]

# Приклад використання:
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_data = heap_sort(data)
print("Відсортований список:", sorted_data)
