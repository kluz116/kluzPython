from Employee import Employee


class JuniorEmployee(Employee):
    def __init__(self,name,age,salary,manager):
        super().__init__(name,age,salary)
        self.manager = manager


junior1 = JuniorEmployee('Allan Musembya', 35, 5004000,'Deborah Kisaale')
print("The Junior Employee First Name :", junior1.name)
print("The Junior Employee Age :", junior1.age)
print("The Junior Employee Salary :", junior1.salary)
print("The Junior Employee Manager :", junior1.manager)

