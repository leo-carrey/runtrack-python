def create_liste():
    L= list(range(1,6))
    print(L)
    L[3]=L[2]+L[4]
    print(L[3])
    print(L[4])

print(create_liste())