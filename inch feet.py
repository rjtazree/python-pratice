def inch (a,b) :
    if a>b :
        i=a-b
    if b>a :
        i=b-a
    if a==b :
        i=0
    
    return i
    
def feet (a,b) :
    if a>b :
        i=a-b
    if b>a :
        i=b-a
    if a==b :
        i=0
    
    return i


print("1st person")

f1= int(input("Enter feet : "))
i1=int(input("Enter inches : "))
print("Height1 : ",f1,"'",i1,"''")
print("2nd person")
f2= int(input("Enter feet : "))
i2=int(input("Enter inches : "))

print("Height2 : ",f2,"'",i2,"''")

print( "Height difference : ",feet(f1,f2),"'",inch(i1,i2),"''")
