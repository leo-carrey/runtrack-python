def reversed_man(word):
    reversed_word=''
    for i in range(1,len(word)+1):
        reversed_word+=word[-i]
    return reversed_word

print(reversed_man('nikana'))