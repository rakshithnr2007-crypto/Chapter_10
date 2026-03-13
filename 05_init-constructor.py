class Employee:    
        # dunder method which automaticall gets called 
    def __init__(self , name, language , salary): # inti get called by itself when object instatiation is done and here arguments which passedd is useful to set or store info
        self.name = name
        self.language = language 
        self.salary = salary

    def getInfo(self):  
        print(f'Name {self.name}, The language is {self.language} The salary is {self.salary}')

    def ask(self):
        print(f"Are you ok {self.name}")

harry = Employee('Harry', 'C++' , 120000)

harry.getInfo()
harry.ask()