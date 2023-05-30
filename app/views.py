from django.shortcuts import render

# Create your views here.

def jinja_conditionals(request):
    d = {
        'a': 24,
        'b': 17,
    }
    return render(request,'jinja_conditionals.html',context=d)