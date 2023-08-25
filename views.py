from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

marks=[
    {
        'name':'sandeep',
        'age':21,
        'result':'PASS'
    },
    {
        'name':'sandy',
        'age':21,
        'result':'FAIL'
    },
    {
        'name':'sunny',
        'age':21,
        'result':'PASS'
    }
]

def home(request):
    context={
        'marks':marks
    }
    return render(request,'sandeep/home.html',context)

def about(request):
    return render(request,'sandeep/about.html')