from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'sweety','age':21,'address':'Tamilnadu'}
    return render(request,'jinja_print.html',context=d)
