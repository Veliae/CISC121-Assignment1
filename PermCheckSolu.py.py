def solution(A):
    # Find the length of the array
    N = len(A)

    # Sort the array from smallest to largest
    A.sort()

    # Check if every number is in the correct order
    for i in range(N):
        # Each number should equal i + 1
        if A[i] != i + 1:
            return 0

    # All numbers are correct
    return 1

