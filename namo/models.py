from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=20, null=True)    # name of subject
    info = models.CharField(max_length=100, null=True)   # info about subject displayed in card-pic
    card_pic = models.ImageField(null=True, blank=True)  # it is the image of the subject

    def __str__(self):
        return self.name


class Question(models.Model):
    ques = models.TextField()
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.CASCADE)
    option1 = models.CharField(max_length=100, null=True)     # 1st opt
    option2 = models.CharField(max_length=100, null=True)     # 2nd opt
    option3 = models.CharField(max_length=100, null=True)     # 3rd opt
    option4 = models.CharField(max_length=100, null=True)     # 4th opt
    correct = models.CharField(max_length=100, null=True)     # correct answer

    def __str__(self):
        return self.ques


class Profile(models.Model):
    anna = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    note = models.CharField(max_length=100, null=True)
    pic = models.ImageField(default="default.png", null=True, blank=True)

    def __str__(self):
        return self.anna.username





