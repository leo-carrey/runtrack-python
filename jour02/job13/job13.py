array = [90,11,25,22,64,34,12]

def my_sort(arr):
    count = 0
    swapped = True
    while swapped:
        swapped = False
        for number in range(len(arr) - 1):
            if arr[number] > arr[number + 1]:
                arr[number], arr[number + 1] = arr[number + 1], arr[number]
                count += 1
                swapped = True
    return arr, count

sorted_list, total_moves = my_sort(array)
print("sorted list :", sorted_list)
print("total number to sort the list :", total_moves)
