from django.shortcuts import render
from blog.calculate import jisuan


def calculate(request):
    return render(request, 'submit.html')


def show(request):
    s = request.POST.get('x')
    result = jisuan(s)
    return render(request, 'submit.html', {'result': result})
