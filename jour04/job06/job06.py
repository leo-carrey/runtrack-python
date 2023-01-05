def create_liste():
    L= list(range(0,5))
    print(L)
    first = L[0]
    last = L[-1]
    L[0] = last
    L[-1] = first
    return L

print(create_liste())