def find_first_position(arr, value_to_count):
    """
    Find the index of the first occurrence of the value in the array
    using binary search.
    """
    left = 0
    right = len(arr) - 1
    first_position = -1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == value_to_count:
            first_position = middle
            right = middle - 1  # keep searching on the left side
        elif arr[middle] < value_to_count:
            left = middle + 1
        else:
            right = middle - 1

    return first_position


def find_last_position(arr, value_to_count):
    """
    Find the index of the last occurrence of the value in the array
    using binary search.
    """
    left = 0
    right = len(arr) - 1
    last_position = -1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == value_to_count:
            last_position = middle
            left = middle + 1   # keep searching on the right side
        elif arr[middle] < value_to_count:
            left = middle + 1
        else:
            right = middle - 1

    return last_position


def count_occurrences_binary(arr, value_to_count):
    """
    Count how many times a given value appears in the array
    using binary search.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    first = find_first_position(arr, value_to_count)

    # If the value does not exist in the array
    if first == -1:
        return 0

    last = find_last_position(arr, value_to_count)

    return last - first + 1


if __name__ == "__main__":
    # Sample input (must be sorted)
    numbers = [1, 1, 2, 4, 5, 5, 7, 9]
    value_to_count = 5

    # Count occurrences using binary search
    result = count_occurrences_binary(numbers, value_to_count)

    # Display result
    print(f"Number of occurrences of {value_to_count} is: {result}")
