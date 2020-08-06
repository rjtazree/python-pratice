#2.	Suppose you have a list [5,7,9,3,6,8,1]. Square those numbers who are odd. Use Single line for loop
list1 = [5,7,9,3,6,8,1] 
  
for i,item in enumerate(list1):    
     if i % 2 != 0: 
       print(item**2) 