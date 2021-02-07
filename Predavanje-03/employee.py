class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def __repr__(self):
        return f'{self.name}, {self.surname}, {self.salary}'

    def prepare_for_file(self):
        return f'{self.name},{self.surname},{self.salary}'

e1 = Employee('Mirko', 'Todorovic' , 500)

f = open('employees.csv','w')

f.writelines(e1.prepare_for_file())

f.close