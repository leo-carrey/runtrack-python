array = [10,20,30,20,10,50,60,40,80,50,40]

def delete_doubles(arr):
    unique_arr = []
    for number in arr:
        if number not in unique_arr:
            unique_arr.append(number)
    return unique_arr

print(delete_doubles(array))
