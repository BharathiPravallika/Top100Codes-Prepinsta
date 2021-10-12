#greatest of two numbers
a, b = map(int, input().split())
if(a > b):
    print("a is greatest")
elif(b > a):
    print("b is greatest")
else:
    print("both are equal")
