class Employee:    
    name = 'Techie'
    language = 'python' 
    salary = 50000 

    def getInfo(self):  # self refers to instance of class # while creatiing methods inside class
        print(f'The language is {self.language} The salary is {self.salary}')

    def ask(self):
        print(f"Are you ok {self.name}")

#if no self it shows one positional argument as shown above class.function(object) 
# it becomes as gets one attribute as object 
# so while defining the function giving self is essential


harry = Employee()
harry.language = 'java'
harry.name = 'Harry'
Employee.getInfo(harry)     # harry.getInfo()  # both are same
harry.ask()