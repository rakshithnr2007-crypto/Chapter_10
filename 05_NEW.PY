class person():
    def __init__(self , name , state, age ):
        self.name = name
        self.state = state
        self.age = age

    def greet(self):
        print(f"Good morning {self.name}")
        
    def info(self): 
        print(f"your from {self.state}")
        print(f'Your age is {self.age}')

raju = person('Raju', 'Delhi' , 34)
raju.greet()
raju.info()