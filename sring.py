from tkinter import N


class String:
    a = "class variable"
    b = "class variable1"
    def __init__(self,p,n): # constructor
        self.name = p   
        self.age = n
    def show(self): #instance method
        c = "Hello" #local variable
        print(c)
        print("Name:-",self.name)
        print("Age:-",self.age)
    @classmethod # decorator
    def show_variable(cls): # class method
        print(cls.a,cls.b)
obj = String("Prakash",27)
obj.show()

