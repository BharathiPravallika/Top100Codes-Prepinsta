#Greatest of the Three numbers: 
a, b, c = map(int, input().split())
if(a>b and a>c):
    print("a is Greatest")
elif(b>a and b>c):
    print("b is Greatest")
elif(c>a and c>b):
    print("c is Greatest")
else:
    print("all are equal")
