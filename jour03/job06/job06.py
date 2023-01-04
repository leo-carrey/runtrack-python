def alpha():
    alphabet=''
    for i in range(97,123):
        alphabet+=chr(i)
    return alphabet

def pyramid(text):
    cursor=1
    while len(text)>cursor:
        print(text[:cursor])
        cursor= cursor+ 1
        text=text[cursor-1:]

    pass

print(pyramid(alpha()*10))