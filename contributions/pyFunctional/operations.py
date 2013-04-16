from company import *

def total(company):

    def totalSubunits(subunits):

        def totalEmployee(employee):
            return employee.salary

        def totalDepartment(department):
            return totalEmployee(department.manager) + totalSubunits(department.subunits)

        return sum(map(lambda s: totalEmployee(s) if isinstance(s, Employee) else totalDepartment(s), subunits))

    return totalSubunits(company.departments)
    
print total(company)

def cut(company):

    def cutSubunit(s):

        def cutEmployee(employee):
            return Employee(employee.name, employee.salary/2.0)

        def cutDepartment(department):
            return Department(department.name, cutEmployee(department.manager), map(cutSubunit, department.subunits))

        return cutEmployee(s) if isinstance(s, Employee) else cutDepartment(s)

    return Company(company.name, map(cutSubunit, company.departments))
    
print total(cut(company))
