# find if the given number is a palindrome or not?
a=int(input("Enter a number"))
b=str(a)
if (b==b[::-1]):
  print(a, " is palindrome")
else:
  print(a, " is not a palindrome number")
  
