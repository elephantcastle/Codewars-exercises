def find_even_index(arr):
    for i,j in enumerate(arr):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    
    return -1