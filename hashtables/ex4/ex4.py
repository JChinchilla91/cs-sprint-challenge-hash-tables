def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    negatives = {}
    result = []

    for num in a:
        if num < 0:
            negatives[-num] = num

    result = [num for num in a if num in negatives]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
