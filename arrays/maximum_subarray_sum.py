def maximum_subarray_sum(A):
    """Uses Kadane's algorithm - dynamic programming

    Args:
        A (list): list of integers
    """

    local_max, global_max = 0, float('-inf') # local max = max(A[i], A[i] + local_max)

    for i in range(len(A)):
        local_max = max(A[i], A[i] + local_max)
        global_max = max(local_max, global_max)

    return global_max



if __name__ == "__main__":
    A = [1,2,3,4]
    print(maximum_subarray_sum(A))