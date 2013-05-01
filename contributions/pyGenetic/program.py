from company import *
from operator import add
import random

# we will cut per department

def fitness(individuals, target):
    s = reduce(add, (i for i in individuals))
    return float(sum(individuals)) / target

def grade(population, target):
    s = reduce(add, (fitness(p, target) for p in population), 0)
    return s / float(len(individuals))

def select(d):
    l = [i[1] for i in d]
    s = sum(l)
    v = random.randint(0, int(s))

    acc = 0
    for (index, item) in enumerate(l):
        if acc >= v:
            return [i for i in d if i[1] == item][0]
        acc += item
    return d[0]

def mutate(rate, m):

    def inner(individual):
        if mutate > random.random:
            return random.randint(0, m)
        else:
            return individual

    return inner

def evolve(population, m, target, mutate_rate=0.01, recombination=0.7):
    d = []

    tmp = population
    population = []
    for individuals in tmp:
        # mutate
        individuals = map(mutate(mutate_rate, m), individuals)
        population.append(individuals)
    
        f = fitness(individuals, target)
        d.append((individuals, f))

    first = select(d)
    d.remove(first)
    second = select(d)

    new = []
    for (f, s) in zip(first[0], second[0]):
        if recombination > random.random():
            new.append((f+s) / 2.0)
        else:
            new.append(random.choice([f, s]))

    population.append(new)
    return population

def generate_salaries(num, target, accuracy):
    accuracy = abs(accuracy - 1)
    m = int(target/num*2.5)
    population = [[random.randint(0, int(target/num*2.5)) for _ in range(num)] for _ in range(num * 10)]
    target = float(target)
    iterations = 0
    while not any(abs((target / float(sum(p))) - 1) < accuracy for p in population):
        population = evolve(population, m, 5)
        iterations += 1

    #print iterations
        
    for p in population:
        if abs((target / float(sum(p))) - 1) < accuracy:
            return p

def cut(company):

    def cutSubunit(s):

        employees = filter(lambda i: isinstance(i, Employee), s.subunits)
        if employees:
            target = sum(map(lambda e: e.salary, employees))
            salaries = generate_salaries(len(employees), target, accuracy=0.99)
            new_employees = []
            for (e, salary) in zip(employees, salaries):
                new_employees.append(Employee(e.name, salary))
            employees = new_employees            


        departments = filter(lambda i: isinstance(i, Department), s.subunits)
        departments = map(cutSubunit, departments)
        return Department(s.name, Employee(s.manager.name, s.manager.salary/2.0), departments + employees)   

    return Company(company.name, map(cutSubunit, company.departments))

def total(company):

    def totalSubunits(subunits):

        def totalEmployee(employee):
            return employee.salary

        def totalDepartment(department):
            return totalEmployee(department.manager) + totalSubunits(department.subunits)

        return sum(map(lambda s: totalEmployee(s) if isinstance(s, Employee) else totalDepartment(s), subunits))

    return totalSubunits(company.departments)


print 'total:', total(company)
print 'after cut:', total(cut(company))
        
