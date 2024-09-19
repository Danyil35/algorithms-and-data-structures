from random import randint


def recursive_max_number(arr, n):
    if (n == 1): 
        return arr[0] 
    return max(arr[n - 1], recursive_max_number(arr, n - 1)) 

array = [randint(-100, 100) for _ in range(40)]
print(f"Array: {array}")
max_element = recursive_max_number(array, len(array))
print(f"Maximum array number: {max_element}")