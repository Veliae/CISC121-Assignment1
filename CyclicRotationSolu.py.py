def solution(A, K):
    # Check if the array is empty
    if len(A) == 0:
        return A

    # Rotate the array K times
    for i in range(K):
        # Remove the last element
        last = A.pop()

        # Put the last element at the beginning
        A.insert(0, last)

    # Return the rotated array
    return A
