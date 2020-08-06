print("Welcome to Grading System")

tup1 = (90,91,92,93,94,95,96,97,98,99,100)
tup2 = (89,88,87,86,85,84,83,82,81,80)
tup3 = (79,78,76,75,74,73,72,71,70)
tup4 = (69,68,67,66,65,64,63,62,61,60)
element = int(input("Enter your obtained result  :  "))
print('\n')
if element in tup1:
    print(" You got A Grade")
if element in tup2:
    print("You got B Grade")
if element in tup3:
    print("You got C Grade")
if element in tup4:
    print("You got D Grade")
