def table_of_multiplication():
    userinput = input("choose a number : ")
    for i in range(1,int(userinput)+1):
        print("La table de multiplication de",i,"est :")
        for n in range(1,11):
            print(n ," x ", i," = ",i*n)

table_of_multiplication()