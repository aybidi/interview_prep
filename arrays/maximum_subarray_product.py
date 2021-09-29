def maximum_subarray_product(A):
    """uses a variant of Kadane's algorithm

    Args:
        A (list): a list of integers
    """

    if len(A) == 0:
        return None
    
    # the idea is similar to maximum subarray sum, but with two catches:
    # a chain could be broke by either a 0 or a negative number
    # if 0, check the result = max(result, max_so_far)
    # if negative, there could be another negative number that will give
    # us a positive product

    # So keep track of current, max_so_far, and min_so_far

    max_so_far = A[0]
    min_so_far = A[0]
    result = max_so_far

    for i in range(1, len(A)):
        current = A[i]
        comparison_list = [current, current * max_so_far, current * min_so_far]
        max_so_far, min_so_far = max(comparison_list), min(comparison_list)

        result = max(result, max_so_far)
    return result