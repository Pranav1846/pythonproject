num=int(input())
rev=0
pal=num
while(num>0):
    rem=int(num%10)
    rev=int(rev*10+rem)
    num=num//10
if (pal==rev):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
        
