class Employee:     # class
    name = 'Techie'
    language = 'python' # class attributes
    salary = 50000 

harry = Employee()      # object instantiation
harry.name = "Harry"    # object attribute / instance attribute
print(harry.name , harry.salary , harry.language)

rohan = Employee()
rohan.name = 'Rohan rao'
print(rohan.name , rohan.language, rohan.salary)

# here name is object attributes and 
# salray and class are class atributes as they directly belongs to class
