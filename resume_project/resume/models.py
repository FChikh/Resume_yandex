from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class GithubConnectedUsers(models.Model):
    id = models.AutoField(primary_key=True)
    authorid = models.IntegerField()
    fullname = models.CharField(max_length=144)
    avatarurl = models.CharField(max_length=244)
    orgs = models.CharField(max_length=90000)
    followers = models.IntegerField()
    repos_dict_with_full_info = models.CharField(max_length=90000)
    moreprofinfo = models.CharField(max_length=90000,default='')
    client_ID_and_secret = models.CharField(max_length=144)
