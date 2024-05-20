#write a program to find the sum of digits of a given number'
a=int(input("Enter a number"))
sum=0
while(a!=0):
    sum=sum+a%10
    a=int(a/10)
print(sum)