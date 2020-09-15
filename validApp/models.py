from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        name_regex = re.compile(r'^[a-zA-Z]+$')

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name is required and must be at least 2 characters"
        if not name_regex.match(postData['first_name']):
            errors['first_name'] = "Name must be only alphanumeric characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name is required and msut be at least 2 characters"
        if len(postData['email']) < 1:
            errors['email'] = "Email is required"
        if not email_regex.match(postData['email']):
            errors['email'] = "Invalid email address"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
