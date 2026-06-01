def SelectionSort(L):
    n = len(L)
    if n <= 1:
        return L
    for i in range(n):
        mpos = i
        for j in range(i + 1, n):
            if L[j] < L[mpos]:
                mpos = j
                # Humne swap ko aapke hi tarike se rakha hai
                (L[i], L[mpos]) = (L[mpos], L[i])
                

    return L


L = [64, 25, 12, 22, 11]
print(SelectionSort(L))