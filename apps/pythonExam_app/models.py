from __future__ import unicode_literals
from django.db import models
import re, bcrypt
import datetime

USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')

# Create your models here.
class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2: #or not postData['first_name'].isalpha():
            errors['name'] = "Input a name longer than 2 Characters"

        if len(postData['username']) < 2: # or not postData['first_name'].isalpha():
            errors['username'] = "Enter an username"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be 8 characters minimum"

        if postData['password'] != postData['confirm']:
            errors['confirm'] = "Passwords do not match!"

        if not USERNAME_REGEX.match(postData['username']):
            errors['pass'] = "Invalid username address"

        try:
            User.objects.get(username = postData['username'])
            errors['duplicate'] = "username already registered"

        except:
            pass


        if len(errors):
            return errors

        else:
            hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())

            user = User.objects.create(
                name = postData['name'],
                username = postData['username'],
                password = hashed_pw,
                )

            return user.id


    def login_validator(self, postData):
            errors ={}

            if len(postData['username']) < 1:
                errors['login_username'] = "Enter an username"

            try:
                user = User.objects.get(username = postData['username'])
                if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                    errors['login_pass'] = "Incorrect Username/Password!"

            except:
                errors['login_val'] = "Login info incorrect!"

            if errors:
                return errors

            else:
                return user.id

class PlanManager(models.Manager):
    def plan_validation(self, postData, user_id):
        errors = {}

        if len(postData['dest']) < 1:
            errors['destination'] = "Enter Destination!"

        if len(postData['desc']) < 1:
            errors['description'] = "Enter Description!"

        if len(postData['startdate']) < 1:
            errors['startdate'] = "Please enter a start date!"

        if len(postData['enddate']) < 1:
            errors['enddate'] = "Please enter a end date!"

        if postData['startdate'] and postData['enddate']:
            start = datetime.datetime.strptime(postData['startdate'], "%Y-%m-%d")
            end = datetime.datetime.strptime(postData['enddate'], "%Y-%m-%d")
            today = datetime.date.today() #format given '2008-11-22 19:53:42'
            today = datetime.datetime(today.year, today.month, today.day) #changes it to '2008-11-22'

            if start < today:
    			errors['startdate']= "We dont support time traveling yet, come back next year"

            if start > end:
                errors['enddate'] = "Your end date comes before start date"

            if end < today:
                errors['enddate'] = "Travel date to must be in the future."

        if errors:
            return errors

        plan = Plan.objects.create(
            dest = postData['dest'],
            desc = postData['desc'],
            users = User.objects.get(id = user_id),
            startdate = postData['startdate'],
            enddate = postData['enddate'],
        )
        return plan.id


    def join_validation(self, postData, tid, uid):
        user1 = User.objects.get(id=uid)
        add = Plan.objects.get(id=tid).many_users.add(user1)
        return add


class User(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Plan(models.Model):
    dest = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    users = models.ForeignKey(User, related_name='plans')
    many_users = models.ManyToManyField(User, related_name = "all_plans")
    startdate = models.DateField()
    enddate = models.DateField()

    objects = PlanManager()
