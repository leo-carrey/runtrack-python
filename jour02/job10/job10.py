start_list = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def round_number(number):
    int_number = int(number)
    x = number - int_number
    if x < 0.5:
        return int_number
    return int_number + 1


def round_list(arr):
    rounded_list = []
    for number in arr:
        rounded_list.append(round_number(number))
    return rounded_list

def sort_list(arr):
    new_arr = []
    while arr != []:
        new_arr.append(min(arr))
        arr.remove(min(arr))
    return new_arr

print(sort_list(round_list(start_list)))
