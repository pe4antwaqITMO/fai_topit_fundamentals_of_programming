import sys
import tracemalloc

# Часть 1
print(sys.getsizeof([]))
print(sys.getsizeof([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sys.getsizeof((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
print(sys.getsizeof("1234567890"))
print(sys.getsizeof(10))
print(sys.getsizeof(None))

# Часть 2
lst = []
old_size = sys.getsizeof(lst)
for i in range(100):
    lst.append(i)
    current_size = sys.getsizeof(lst)
    if current_size != old_size:
        print(len(lst), current_size)
        old_size = current_size

# Часть 3
tracemalloc.start()
numbers_list = list(range(100_000))
curr, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(curr / 1024, peak / 1024)

tracemalloc.start()
numbers_range = range(100_000)
curr, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(curr / 1024, peak / 1024)
