a=input()
s={"a","e","i","o","u","A","E","I","O","U"}
count=0
for i in (a):
    if i in s:
        count+=1
if count==0:
    print("No vowels were found.")
else:
    print("Total number of vowels:",count)            
        
    
