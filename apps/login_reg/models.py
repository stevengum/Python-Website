from __future__ import unicode_literals
import re, bcrypt
from django.db import models

class UserManager(models.Manager):
    def validateLogin(self,params):
        user = self.filter(username=params['username'])
        if user:
            if bcrypt.hashpw(params['password'].encode(), user[0].password.encode()) == user[0].password: ## this checks the password against the hash
                return (True, user[0])
        else:
            return ('Username or password are incorrect (or both)', 'error')



    def register(self,params):
        errors = []
        ## if user: checks if the username is already inside the table
        if len(params['name']) < 3:
            errors.append(("Your name is shorter than 3 characters, is this actually your name?", "name"))
        if len(params['username']) < 3:
            errors.append(("Your username must be longer than 3 characters, sorry, not sorry.", "last_name"))
        elif self.filter(username=params['username']).exists():
            errors.append(("Username already taken!", "username"))

        if len(params['password']) < 8:
            errors.append(("Your password is too short!", "password"))
        if params['password'] != params['confirm_pw']:
            errors.append(("Your passwords do not match!", "password"))
        if errors:          ##empty list counts as false
            return (False,errors)
            #jack returns a dictionary called { "errors" : errors}
            #when using dicitionaries, then we could check if the key exists using the "if 'keyname' in dictionary_name:"

        ## if passes previous checks
        newpassword = bcrypt.hashpw(params['password'].encode(),bcrypt.gensalt())
        newuser = self.create(name=params['name'], username=params['username'],password=newpassword)
        return (True, newuser)

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=40, default="foo")
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
