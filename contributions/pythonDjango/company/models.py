from django.db import models

# Create your models here.
#
#class Company(models.Model):
#
#    name = models.CharField(max_length=200)
#
#class Department(models.Model):
#
#    name = models.CharField(max_length=200)
#
#    upper = models.ForeignKey('Department')
#    company = models.ForeignKey(Company)
#
#
#class Employee(models.Model):
#
#    name = models.CharField(max_length=200)
#    address = models.CharField(max_length=100)
#    salary = models.IntegerField()
#
#    department = models.ForeignKey(Department)

class Company:
    def __init__(self, name, depts):
        self.name = name
        self.depts = depts

    def cut(self):
        [dept.cut() for dept in self.depts]

    def total(self):
        return sum(dept.total() for dept in self.depts)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_dept(self, name):
        return filter(bool, (d.get_dept(name) for d in self.depts))[0]

    def get_employee(self, name):
        return filter(bool, (d.get_employee(name) for d in self.depts))[0]

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def cut(self):
        self.salary = self.salary / 2.0

    def total(self):
        return self.salary

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_dept(self, name):
        return None

    def get_employee(self, name):
        return self if self.name == name else None

class Dept:
    def __init__(self, name, manager, subunits, employees):
        self.name = name
        self.manager = manager
        self.subunits = subunits
        self.employees = employees

    def cut(self):
        self.manager.cut()
        
        for subunit in self.subunits:
            subunit.cut()
         
        for e in self.employees:
            e.cut()

    def total(self):
        return self.manager.total() + sum(e.total() for e in self.employees) + sum(subunit.total() for subunit in self.subunits)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_dept(self, name):
        if self.name == name:
            return self
        
        if len(self.subunits) == 0:
            return None
        
        d = filter(bool, (d.get_dept(name) for d in self.subunits))
        if d:
            return d[0]
        else:
            return None        
    

    def get_employee(self, name):
        own = filter(lambda e: e.name == name, self.employees + [self.manager])
        if own:
            return own[0]
        else:
            return reduce(lambda x, y: x or y, [d.get_employee(name) for d in self.subunits]) if self.subunits else []

company = Company(
    name = "Meganalysis",
    depts = [
        Dept(
            name = "Research",
            manager = Employee(
                name = "Craig",
                salary = 123456.0
            ),
            subunits = [
                
            ],
            employees = [
                Employee(
                    name = "Erik",
                    salary = 12345.0
                ),
                Employee(
                    name = "Ralf",
                    salary = 1234.0
                )
            ]
        ),
        Dept(
            name = "Development",
            manager = Employee(
                name = "Ray",
                salary = 234567.0
            ),
            subunits = [
                Dept(
                    name = "Dev1",
                    manager = Employee(
                        name = "Klaus",
                        salary = 23456.0
                    ),
                    subunits = [
                        Dept(
                            name = "Dev1.1",
                            manager = Employee(
                                name = "Karl",
                                salary = 2345.0
                            ),
                            subunits = [],
                            employees = []
                        )
                    ],
                    employees = []
                ),
                
            ],
            employees = [
                Employee(
                    name = "Joe",
                    salary = 2344.0
                )
            ]
        )
    ]
)





