# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def registerVal(self, postData):
        results = {"valid": True, "errors": []}
        if not postData['name'] or len(postData['name']) < 3:
            results['errors'].append("Name is not valid")
            results['valid'] = False
        if not postData['username'] or len(postData['username']) < 3:
            results['errors'].append("Username is not valid")
            results['valid'] = False
        if not postData['pass'] or len(postData['pass']) < 8:
            results['errors'].append("Password must be at least 8 characters")
            results['valid'] = False
        if postData['pass'] != postData['confirm']:
            results['errors'].append("Passwords must match")
            results['valid'] = False
        if results['valid']:
            if len(User.objects.filter(username = postData['username'])) != 0:
                results['errors'].append("Please try another username")
                results['valid'] = False
            else: 
                hashed = bcrypt.hashpw(postData['pass'].encode('utf-8'), bcrypt.gensalt())
                User.objects.create(name = postData['name'], username = postData['username'],  password = hashed)
        return results
    def loginVal(self, postData):
        results = {"valid": True, "errors": []}
        if len(User.objects.filter(username = postData['login_username'])) == 0:
            results['errors'].append("No username found")
            results['valid'] = False
        else: 
            hashed = bcrypt.hashpw(postData['login_pass'].encode('utf-8'), User.objects.filter(username = postData['login_username'])[0].password.encode('utf-8'))
            if User.objects.filter(username = postData['login_username'])[0].password != hashed:
                results['errors'].append("Incorrect Password")
                results['valid'] = False
        return results

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    def __str__(self):
        return self.name + " "  + self.password