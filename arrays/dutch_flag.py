def dutch_flag(A, index):
    smaller, equal, larger = 0, 0, len(A)
    pivot = A[index]
    while equal < larger:
        if A[equal] < pivot:
            A[equal], A[smaller] = A[smaller], A[equal]
            equal, smaller = equal + 1, smaller + 1
        elif A[equal] == pivot:
            equal = equal + 1
        else:
            larger = larger -1
            A[equal], A[larger] = A[larger], A[equal]
    return A

print(dutch_flag([6,5,4,3,2,1], 1))