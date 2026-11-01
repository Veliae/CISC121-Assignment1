def solution(A):
    # Count eastbound cars and passing pairs
    east = 0
    pairs = 0

    # Go through each car in the array
    for car in A:
        if car == 0:
            # Count an eastbound car
            east = east + 1
        else:
            # Add passing pairs for westbound car
            pairs = pairs + east

        # Check if pairs exceed the limit
        if pairs > 1000000000:
            return -1

    # Return total passing pairs
    return pairs
