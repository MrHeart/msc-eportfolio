def linear_search(arr, target):
    """
    Perform a linear search on a list.

    :param arr: List of elements to search within
    :param target: The element to search for
    :return: Index of the target element if found, otherwise -1
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
arr = [10, 20, 30, 40, 50]
target = 30
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
