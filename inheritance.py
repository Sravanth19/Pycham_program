class Employee:
    def work(self):
        print("Employee is working.")
class Manager(Employee):
    def manage(self):
        print("Manager is managing the team.")
e=Employee()
e.work()
m=Manager()
m.work()
m.manage()
