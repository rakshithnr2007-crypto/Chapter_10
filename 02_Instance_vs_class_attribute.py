class Employee:     # class
    name = 'Techie'
    language = 'python' # class attributes
    salary = 50000 

harry = Employee()      # object instantiation
harry.name = "Harry"    # object attribute / instance attribute
harry.language = 'java'  # updatinng the attribute by instance attribute
print(harry.name , harry.salary , harry.language)

print(Employee.name)