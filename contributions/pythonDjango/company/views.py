# Create your views here.
from django.http import HttpResponse
from company.models import company, Dept, Company, Employee
from django.template import Context, loader
from django.shortcuts import render_to_response, redirect

def index(request):
    return render_to_response('index.html', { 'company' : company })
    

def department(request, department_name):

    dept = company.get_dept(department_name)
    return render_to_response('department.html', { 'dept' : dept })

def employee(request, employee_name):

    e = company.get_employee(employee_name)
    return render_to_response('employee.html', { 'e' : e})

def cut(request):
    
    company.cut()
    return redirect('/company/total')

def total(request):
    return render_to_response('total.html', {'value': company.total()})
    
    

