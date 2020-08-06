def s(input_string,find):
    res = None
    for i in range(0, len(input_string)): 
        if input_string[i] == find: 
            res = i + 1
            break
      
    if res == None: 
        print ("No such charater available in string") 
    else: 
        print ("Character {} is present at {}".format(find, str(res))) 
        
        
input_string= input()
  
find=input()

print ("initial_string : ", input_string, "\ncharacter_to_find : ", find) 

s(input_string,find)