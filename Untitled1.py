#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class studentform:
    def __init__(self,name,fname,age,rollno,education,gender,cnic):
        self.name = name
        self.fname = fname
        self.age = age
        self.rollno = rollno
        self.education = education
        self.gender = gender
        self.cnic = cnic
    def __cnic(self):
#         dont expose the cnic
        print(f"{self.name} cnic is {self.cnic} which is private ")
    def show(self):
        print(f"STUDENT INFO IS: \nNAME: {self.name}\nFATHER NAME: {self.fname}\nAGE: {self.age}\nROLLNO: 
              {self.rollno}\nLEVEL OF EDUCATION: {self.education}\nGENDER: {self.gender}\n")


obj1 = studentform("Kaif","Asif","19","19","BSAI","Male","42301-8982341-1")
obj1.show()
# calling private methode forcefully
obj1._studentform__cnic() 

# PUBLIC IN ENCAPSULATION

class Feechallan(studentform):
    def feechallan(self,feechallan):
        self.feechallan = feechallan
        print(f"THE FEECHALLAN ISSUED TO {self.name} IS : {self.feechallan}")
        
obj2 =  Feechallan("sherry","Ahmed","21","28","BSAI","Male","42301-8982341-1")
obj2.show()
obj2.feechallan("789900")

# protected methode
class result(studentform):
    def _result(self,math,physics,computer):
        self.math = math
        self.phy = physics
        self.computer = computer
        average = int(math+physics+computer)//3
        print("THE RESULT IS", +average)
        
  
    
obj3 =  result("sherry","Ahmed","21","28","BSAI","Male","42301-8982341-1")
obj3.show()
obj3._result(69,45,89)

    


# In[2]:



class studentform:
    def __init__(self,name,fname,age,rollno,education,gender,cnic):
        self.name = name
        self.fname = fname
        self.age = age
        self.rollno = rollno
        self.education = education
        self.gender = gender
        self.cnic = cnic
    def __cnic(self):
#         dont expose the cnic
        print(f"{self.name} cnic is {self.cnic} which is private ")
    def show(self):
        print(f"STUDENT INFO IS: \nNAME: {self.name}\nFATHER NAME: {self.fname}\nAGE: {self.age}\nROLLNO: {self.rollno}\nLEVEL OF EDUCATION: {self.education}\nGENDER: {self.gender}\n")


obj1 = studentform("Kaif","Asif","19","19","BSAI","Male","42301-8982341-1")
obj1.show()
# calling private methode forcefully
obj1._studentform__cnic() 


# In[ ]:




