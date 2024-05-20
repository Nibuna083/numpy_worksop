#write a program to find if the given number is prime no or not
a=int(input("enter number"))
count=0
for i in range (2,a):
    if(a%i==0):
        count+=1
if(count!=0):
    print("consonant")
else:
    print("prime")
