from django.shortcuts import render

# Create your views here.
def lion(request):
    return render(request,'image.html')
