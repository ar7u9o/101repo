from syb import *
import operator



class Company:
    def __init__(self, name, depts):
        self.name = name
        self.depts = depts

    def __str__(self):
        return 'Company {} {}'.format(self.name, map(str, self.depts))

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return 'Employee {} {}'.format(self.name, self.salary)

class Dept:
    def __init__(self, name, manager, subunits):
        self.name = name
        self.manager = manager
        self.subunits = subunits

    def __str__(self):
        return 'Company "{}" ({}) [{}]'.format(self.name, self.manager, ', '.join(map(str, self.subunits)))

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
                            subunits = [
                                Employee(
                                    name = "Joe",
                                    salary = 2344.0
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)




total = everything(operator.add, (0 |mkQ| special_id(float)))
t_sum = total(company)
assert t_sum == 399747.0

@t(Employee)
def incS(e):
    return Employee(e.name, e.salary * 2.0)

increase = everywhere(mkT(incS))
c = increase(company)

assert total(c) == total(company) * 2.0

def findD(n):

    @t(Dept)
    def inner_findD(d):
        if d.name == n:
            return Just(d)
        else:
            return Nothing()

    return inner_findD


find = lambda n, k: everything(orElse, (Nothing() |mkQ| (findD(n))))(k)

assert find('Research', company).value.name == 'Research'

# example from 6.2 hmap.hs

@t(Company)
def isDept(n, k):
    return partial(False |mkQ| partial(isDeptD, n), k)

def isDeptD(n, d):
    return d.name == n

def incrOne(n, k):
    if isDept(n, k):
        return increase(k)
    else:
        return gmapT(partial(incrOne, n), k)

research = find('Research', company)
research_total = total(research)

after_research = total(find('Research', incrOne('Research', company)))

assert research_total * 2 == after_research

# simplification

def incrOneEasy(n, k):

    @t(Company)
    def rightCompany(c):
        return c.name == n
    
    f = False |mkQ| rightCompany

    return everywhereBut(f, mkT(incS))(k)

research = find('Research', company)
research_total = total(research)

after_research = total(find('Research', incrOneEasy('Research', company)))


assert research_total * 2 == after_research

# example

@t(object)
def hcG(arg):
    return [arg]

@t(Dept)
def hcD(d):
    return ['d', d]

@t(Employee)
def hcP(p):
    return ['e', p]

def hc(k):
    return everything(operator.add, hcG |extQ| hcP |extQ| hcD)(k)

c = hc(company)

size = gsize(company)
