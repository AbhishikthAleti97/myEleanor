from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    numbers = [1,2,3,4]
    name = "Abhishikth"
    args = {'Name':name,'numbers':numbers}
    return render(request,'accounts/home.html',args)