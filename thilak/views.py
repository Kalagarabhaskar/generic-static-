from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request,'mainpage.html')




def login_form(request):
    return render(request,'login_form.html')





def signup_form(request):
    return render(request,'signup_form.html')