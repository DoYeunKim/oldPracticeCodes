# min heap: each parent node is <= to its child
# max heap: each parent node is >= to its child
"""
    heapify: converts a regular list to a heap; smallest at [0], but the rest not necessarily sorted
    heappush: push an element w/o altering the current heap
    heappop: returns the smallest data element
    heapreplace: replace the smallest data w/ a new value
"""

import heapq

H = [21,1,45,78,3,5]
heapq.heapify(H)
print(H)

# Inserting into heap
heapq.heappush(H, 8)
print (H)

# Removing from heap
heapq.heappop(H)
print(H)

# Replacing heap
heapq.heapreplace(H, 17)
print(H)