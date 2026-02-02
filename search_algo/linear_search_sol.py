def count_linear(arr, value_to_count):
    """
    Count how many times a given value appears in the array
    using a simple linear scan.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    count = 0

    # Go through each element in the array
    for value in arr:
        if value == value_to_count:
            count += 1

    return count


if __name__ == "__main__":
    # Sample input
    numbers = [1, 1, 2, 4, 5, 5, 7, 9]
    value_to_count = 5

    # Count occurrences
    result = count_linear(numbers, value_to_count)

    # Display result
    print(f"Number of occurrences of {value_to_count} is: {result}")
