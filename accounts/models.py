from django.db import models

# Create your models here.



class Accounts(models.Model):
	email =  models.EmailField(max_length = 200)
	password  = models.CharField(max_length=200)
	password_confirm = models.CharField(max_length=200)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	gender = models.CharField(max_length=20)
	country = models.CharField(max_length=100)