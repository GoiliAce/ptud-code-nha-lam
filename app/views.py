from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"app/home.html")
def cv1(request):
    return render(request,"app/cv1.html")
def cv2(request):
    return render(request,"app/cv2.html")
def todo1(request):
    return render(request,"app/todo1.html")
def todo2(request):
    return render(request,"app/todo2.html")

