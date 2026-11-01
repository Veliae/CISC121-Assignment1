def solution(A):
    # Find the total sum of the array
    total = sum(A)

    # Start with an empty left side
    left = 0
    minDiff = float('inf')

    # Try every possible split
    for i in range(len(A) - 1):
        # Add current number to the left side
        left = left + A[i]

        # Find the sum of the right side
        right = total - left

        # Calculate the absolute difference
        diff = abs(left - right)

        # Update minimum difference
        if diff < minDiff:
            minDiff = diff

    # Return the smallest difference
    return minDiff
