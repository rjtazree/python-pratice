#fibonacci
a=int(input("Enter the number"))
f=0                                         #first element of series
s=1                                         #second element of series
if a<=0:
    print("The series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next