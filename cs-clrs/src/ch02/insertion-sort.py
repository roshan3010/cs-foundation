def insertion_sort(A):
    for j in range(1, len(A)):
        key=A[j]
        i=j-1
        while (i>=0 and A[i]>key):
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
    return A

A = [5,32,2,9,-2,99]
print(insertion_sort(A))
