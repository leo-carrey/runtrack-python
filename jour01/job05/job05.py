

def what_do_you_whant():
    name = "chiken"
    price = 5
    quantity_in_stock = 269
    print(f"name : {name}, price : {price}, quantity_in_stock : {quantity_in_stock}")
    userinput = input("what quantity you want ? :")
    quantity_in_stock = quantity_in_stock - int(userinput)
    print(quantity_in_stock)
    # INFLATION !!!
    price = price*1.10
    print(price)

what_do_you_whant()
