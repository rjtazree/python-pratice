#average from best 2
mark1=int(input("Enter first mark : "))
mark2=int(input("Enter second mark : "))
mark3=int(input("Enter third mark : "))

def avg (a,b):
    print("Best two marks are : ",a,",",b)
    print("Average : ", float((a+b)/2))
    
if mark1>mark2 and mark2>mark3 :
   avg(mark1,mark2)
if mark1>mark2 and mark3>mark2 :
   avg(mark1,mark3)
if mark2>mark1 and mark1>mark3 :
   avg(mark2,mark1)
if mark2>mark3 and mark3>mark1 :
   avg(mark2,mark3)
if mark3>mark1 and mark1>mark2 :
   avg(mark3,mark1)
if mark3>mark2 and mark2>mark1 :
   avg(mark3,mark2)