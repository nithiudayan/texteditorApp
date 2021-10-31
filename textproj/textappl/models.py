from django.db import models
class login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    role=models.IntegerField()

class registration(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    logid=models.ForeignKey(login,on_delete=models.CASCADE)

class tagtbl(models.Model):
    tag=models.CharField(max_length=200)

class textsnippettbl(models.Model):
    text=models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    user= models.CharField(max_length=200)
    tagid=models.ForeignKey(tagtbl,on_delete=models.CASCADE)
