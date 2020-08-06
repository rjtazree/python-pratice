#1.	Write e recursive function to calculate sum of all elements in a range.
#For example, you have a function named recursive_sum(a,b) , a=5, b=10. The function will return 5+6+7+8+9+10=45 

def recursive_sum(a,b):
    if(a<=b):
        ans= a + recursive_sum(a+1,b)
    else:
        ans=0
    return ans


summ = recursive_sum(5,10)
print("\nSummation : ", summ) 