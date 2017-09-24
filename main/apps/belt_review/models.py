from __future__ import unicode_literals
import re
from django.db import models

emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


class userManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        print postData
        for input in postData:
            if len(postData[input]) < 2:
                errors['input'] = "All fields are required"
            # elif not postData['name'].isalpha():
            #     errors['name'] = "Invalid  name!"
            # elif not postData['alias'].isalpha():
            #     errors['alias'] = "Invalid  alias!"
            elif not emailRegex.match(postData['email']):
                errors['email'] = "Invalid  email!"
            elif postData['password'] < 8:
                errors['password'] = "Invalid password..."
            elif postData['password'] != postData['confirm_password']:
                errors['confirm_password'] = "Passwords dont match!"
            return errors

    def login_validator(self, postData):
        errors = {}
        for input in postData:
            if len(postData[input]) < 2:
                errors['input'] = "All fields are required"
            elif not emailRegex.match(postData['email']):
                errors['email'] = "Invalid  email!"
            elif postData['password'] < 8:
                errors['password'] = "Invalid password..."
            return errors


class user(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    objects = userManager()

    def __repr__(self):
        return "<user object: {} {} {}>".format(self.name, self.alias, self.email)

class author(models.Model):
    author = models.CharField(max_length=255)

    def __repr__(self):
        return "<book object: {}>".format(self.author)
    
class book(models.Model):
    title = models.CharField(max_length=255)
    author_id = models.ForeignKey(author, related_name="book_id", null=True)

    def __repr__(self):
        return "<book object: {}>".format(self.title)

class review(models.Model):
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users_id = models.ForeignKey(user, related_name="book_id")
    books_id = models.ForeignKey(book, related_name="review_id")

    def __repr__(self):
        return "<review object: {} {}>".format(self.rating, self.review)

