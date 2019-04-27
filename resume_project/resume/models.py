from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Github_connected_users(models.Model):
  id = models.AutoField(primary_key=True)
  authorid = models.IntegerField()
  fullname = models.CharField(max_length=144)
  avatarurl = models.CharField(max_length=244)
  orgs = models.CharField(max_length=90000)
  followers = models.IntegerField()
  repos_dict_with_full_info = models.CharField(max_length=90000)
  client_ID_and_secret = models.CharField(max_length=144)