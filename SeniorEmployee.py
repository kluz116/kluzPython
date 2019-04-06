from Employee import Employee


class SeniorEmployee(Employee):
    number_of_cars = 5

    def __init__(self, name, age, salary, privillages):
        super().__init__(name, age, salary)
        self.privillages = privillages

    def getNumberOfCars(self):
        return self.number_of_cars * 10


sn1 = SeniorEmployee('Richard Sekibuule', 39, 300000, 'He can Withdraw Any Amount Of Money')
print('Senior employee Name :', sn1.name)
print('Senior employee Salary :', sn1.salary)
print('Senior employee Age :', sn1.age)
print('Senior Staff Privileges :', sn1.privillages)

print('Senior Number Of Cars :', sn1.number_of_cars)
print('Senior Managment Number Of Cars :', sn1.getNumberOfCars())