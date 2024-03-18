input_a = int(input("input a number :"))
input_b = int(input("input a number :"))
input_c = int(input("input a number :"))

if input_c**2 == input_a**2 + input_b**2:
    print("the triangle is right-angled")

elif input_a == input_b != input_c or input_a == input_c != input_b or input_b == input_c != input_a:
    print("the triangle is isosceles")

elif input_a == input_b == input_c:
    print("this triangle is equilateral")

elif input_a < input_b + input_c and input_b < input_a + input_c and input_c < input_a + input_b:
    print("this triangle is any")

else:
    print("its not a triangle")
    
