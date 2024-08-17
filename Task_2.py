import heapq

def merge_k_lists(lists):
    min_heap = []
    # Додаємо перший елемент кожного списку в купу
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    merged_list = []
    while min_heap:
        val, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(val)
        # Додаємо наступний елемент з того ж списку в купу
        if element_index + 1 < len(lists[list_index]):
            next_val = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_val, list_index, element_index + 1))
    
    return merged_list

# Приклад використання:
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
