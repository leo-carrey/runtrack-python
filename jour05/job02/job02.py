def draw_rectangle(w,h):
    print("|", "-" * (w - 2), "|")
    for i in range (h - 2):
        print("|", " " * (w - 2), "|")
    print("|", "-" * (w - 2), "|")

draw_rectangle(10,3)



# w = int(input('Please Enter the height of the Rectangle: '))
# h = int(input('Please Enter the Width of the Rectangle: '))
# print("|", "-" * (w - 2), "|")
# for i in range (h - 2):
#     print("|", " " * (w - 2), "|")
# print("|", "-" * (w - 2), "|")