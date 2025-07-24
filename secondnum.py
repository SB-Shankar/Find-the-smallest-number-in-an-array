arr = [5, 3, 8, 1, 9, 3, 9]
unique_sorted = sorted(set(arr))  

if len(unique_sorted) >= 2:
    second_smallest = unique_sorted[1]
    second_largest = unique_sorted[-2]
    print("Second Smallest:", second_smallest)
    print("Second Largest:", second_largest)
else:
    print("Array does not have enough unique elements.")
