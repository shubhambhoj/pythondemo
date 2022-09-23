class String:
    a = "class variable"
    b = "class variable1"
    def __init__(self,p,n): # init Method & constructor
        self.name = p   
        self.age = n
    def show(self): #instance method
        c = "Data" #local variable
        print(c)
        print(f"Name:-{self.name}")
        print(f"Age:-{self.age}")
    @classmethod # decorator
    def show_variable(cls): # class method
        print("1st  {} and 2nd  {}".format(cls.a,cls.b))
obj1 = String("Prakash",27)
obj2 = String("Abhishek",24)

obj1.show()
obj2.show()
print()
obj2.show_variable()
