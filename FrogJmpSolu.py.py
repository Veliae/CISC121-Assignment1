def solution(X, Y, D):
    # Calculate the distance the frog needs to travel
    distance = Y - X

    # Calculate the number of full jumps
    jumps = distance // D

    # Add one more jump if there is a remainder
    if distance % D != 0:
        jumps = jumps + 1

    # Return the minimum number of jumps
    return jumps
