import numpy as np

arr = np.arange(1, 11)

print("Original Array:")
print(arr)

# 2. Slicing operations
print("\nSlicing Operations:")

print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[5:])
print("Elements from index 2 to 6:", arr[2:7])
print("Every second element:", arr[::2])

# 3. Statistical measures
print("\nStatistical Measures:")

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 4. Broadcasting
arr_broadcast = arr + 5

print("\nAfter Broadcasting (adding 5):")
print(arr_broadcast)

arr_broadcast = arr * 2

print("\nAfter Broadcasting (multiplying by 2):")
print(arr_broadcast)
