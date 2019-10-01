a=0
b=1
n=int(input("Enter a number \n"))
print(a," " ,end='')
print(b," ",end='')
for i in range(1,n-1):
    c=a+b
    print(c,' ',end='')
    a=b
    b=c
