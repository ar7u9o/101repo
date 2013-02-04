# Create your views here.
from django.http import HttpResponse
from company.models import company, Dept, Company, Employee
from django.template import Context, loader
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html', { 'company' : company })
    

def department(request, department_name):

    def get_dept(o, name):
        if isinstance(o, Company):
            return reduce(lambda a, b: a if a else b, [get_dept(c, name) for c in o.depts])

        elif isinstance(o, Dept):
            if o.name == name:
                return o
            else:
                return reduce(lambda a, b: a if a else b, [get_dept(c, name) for c in o.subunits])

        elif isinstance(o, Employee):
            return None

    dept = get_dept(company, department_name)

    for s in dept.subunits:
        if isinstance(s, Dept):
            s.type = 'Dept'
        else:
            s.type = 'Employee'
    
    return render_to_response('department.html', { 'dept' : dept })

def employee(request, employee_name):
    def get_employee(o, name):
        if isinstance(o, Company):
            return reduce(lambda a, b: a if a else b, [get_employee(c, name) for c in o.depts])

        elif isinstance(o, Dept):
            return reduce(lambda a, b: a if a else b, [get_employee(c, name) for c in o.subunits])

        elif isinstance(o, Employee):
            return o if o.name == name else None

    e = get_employee(company, employee_name)
    return HttpResponse('Name: ' + e.name)

def cut(request):
    
    company.cut()
    

