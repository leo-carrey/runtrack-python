def multiple_2(n):
    count = 1
    for i in n:
        if i % 2 == 0:
            count = count * i
    return count

print(multiple_2([8, 24, 27, 48, 2,16, 9, 7, 84, 91]))