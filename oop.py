class Employee:


        def __init__(self,name,age,salary):
            self.name = name
            self.age = age
            self.salary = salary

        def getSalary(self):
            return  self.salary

        def getNetSalary(self):

            return  int(self.salary-1500)


emp1 = Employee('Allan Musembya',15,25000)
emp2 = Employee('Kluz williams',24,50000)
print('The Salary Is :',emp1.salary)
print('The age Is :',emp1.age)
print('The Name Is :',emp1.name)

print('Get Salary With A Method :',emp1.getSalary())
print('Get Salary After Taxation:',emp1.getNetSalary())
print('Get Salary With A Method :',emp2.getSalary())
print('Get Salary After Taxation:',emp2.getNetSalary())

