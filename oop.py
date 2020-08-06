
class Employ:  
    def __init__(self, name, adrs,mobile,salary):  
        self.name = name  
        self.adrs = adrs  
        self.mobile = mobile  
        self.salary = salary  
    
    def __repr__(self):  
        return "name:% s , Address:% s , Mobile:% s , Salary:% s" % (self.name, self.adrs, self.mobile , self.salary )  
              
emp1 = Employ("taz","ctg", +880184 , 5000)  
print(emp1) 
