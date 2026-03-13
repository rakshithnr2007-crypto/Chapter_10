class Employee:    
    name = 'Techie'
    language = 'python' 
    salary = 50000 

    def getInfo(self):  
        print(f'The language is {self.language} The salary is {self.salary}')

    @staticmethod  # decorator to mark as a static method
    def ask():
        print(f"Are you ok")
# it does not need self argument it gets exhicute by itself
# where in such static methods attributes cannot be utilized or called 
# when no necessary of object inside functionn nd if we dont call any attribute that time static method is used so it no need of self parameter


naveen = Employee()
print(naveen.ask() , naveen.getInfo())