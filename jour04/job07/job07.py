def multiple_3(n):
    count = 0
    for i in n:
        if i % 3 == 0:
            count = count + 1
    return count

print(multiple_3([8,24,48,2,16]))