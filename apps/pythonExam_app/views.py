from django.shortcuts import render, redirect
from .models import User, Plan
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "pythonExam_app/index.html")

def dashboard(request):
    try: #checks is user is logged in.
        request.session['user_id']
    except:
        return redirect('/')
    context = {
        "users": User.objects.all(),
        "welcome": User.objects.get(id = request.session['user_id']),
        "mytrips": Plan.objects.filter(users__id = request.session['user_id']),
        "all_trips": Plan.objects.all(),
        'trips': Plan.objects.filter(many_users__id=request.session['user_id']) | Plan.objects.filter(users__id = request.session['user_id']),
        }

    return render(request, "pythonExam_app/dashboard.html", context)

def reg_process(request):
    errors = User.objects.registration_validator(request.POST)
    if type(errors) == dict:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    request.session['user_id'] = errors
    return redirect('/dashboard')

def login_process(request):
    errors = User.objects.login_validator(request.POST)
    if type(errors) == dict:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    request.session['user_id'] = errors
    return redirect('/dashboard')


def logout(request):
    request.session.clear()
    return redirect('/')


def addTravel(request):
    return render(request, "pythonExam_app/addTravel.html")

def addTravel_process(request):
    print request.session['user_id']
    errors = Plan.objects.plan_validation(request.POST, request.session['user_id'])
    if type(errors) == dict:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/addTravel')
    return redirect("/dashboard")

# def delete(request, id):
#     cancel = Plan.objects.get(id = id)
#     cancel.delete()
#     return redirect('/dashboard')

def join(request, tid):
    errors = Plan.objects.join_validation(request.POST, tid, request.session['user_id'])
    return redirect('/dashboard')

def show(request, tid):

    context = {
        "trips": Plan.objects.get(id = tid),
        "others": User.objects.filter(all_plans__id = tid),
    }
    return render(request, "pythonExam_app/show.html", context)
