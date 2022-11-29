import heapq


def merge_k_sorted(arrs: list) -> list:
    pq = arrs
    heapq.heapify(pq)
    res = []
    while pq:
        min = heapq.heappop(pq)
        res.append(min.pop(0))
        if min:
            heapq.heappush(pq, min)
    return res
