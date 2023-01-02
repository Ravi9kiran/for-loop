from django.shortcuts import render

# Create your views here.
def Ravi(request):
    d={'name':'Kiran'}
    return render(request,'Ravi.html',d)