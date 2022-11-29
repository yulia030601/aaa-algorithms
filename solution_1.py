def min_heapify(arr: list, i: int):
    left = i * 2 + 1
    right = i * 2 + 2
    if left >= len(arr):
        return
    if len(arr) > right and arr[left] > arr[right]:
        index_to_swap = right
        value_to_swap = arr[right]
    else:
        index_to_swap = left
        value_to_swap = arr[left]
    if arr[i] > value_to_swap:
        arr[i], arr[index_to_swap] = arr[index_to_swap], arr[i]
        min_heapify(arr, index_to_swap)


def build_min_heap(arr: list):
    for i in range(len(arr) // 2, -1, -1):
        min_heapify(arr, i)


def min_heapify_sized(arr: list, i: int, size: int):
    left = i * 2 + 1
    right = i * 2 + 2

    if left >= size:
        return

    if size > right and arr[left] > arr[right]:
        index_to_swap = right
        value_to_swap = arr[right]
    else:
        index_to_swap = left
        value_to_swap = arr[left]

    if arr[i] > value_to_swap:
        arr[i], arr[index_to_swap] = arr[index_to_swap], arr[i]
        min_heapify_sized(arr, index_to_swap, size)


def get_kth_element(arr: list, k: int):
    build_min_heap(arr)
    for i in range(len(arr) - 1, len(arr) - k - 2, -1):
        arr[0], arr[i] = arr[i], arr[0]
        min_heapify_sized(arr, 0, i)
    return arr[i]


if __name__ == '__main__':
    a = [3, 1, 2, 4]
    el = 2
    print(get_kth_element(a, el))




