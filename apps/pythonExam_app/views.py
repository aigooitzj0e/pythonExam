from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "pythonExam_app/index.html")
