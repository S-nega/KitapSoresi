from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateField(['%d-%m-%Y'])#???
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    info = models.TextField(blank=True)#не обязательно к заполнению
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    role = models.BooleanField(default=False) #False=user; True=admin

    def __str__(self):
        return self.name

class Friends(models.Model):
    userId = models.IntegerField(blank=False)#обязательно к заполнению, заполняется автоматически в бэке
    followerId = models.IntegerField(blank=False)#обязательно к заполнению, заполняется автоматически в бэке

class News(models.Model):
    authorId = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="newsPhotos/%Y/%m/%d")
    text = models.TextField(blank=True)#не обязательно к заполнению
    bookId = models.IntegerField(blank=True)#не обязательно к заполнению
    saveStatus = models.BooleanField(default=False)

class StarList(models.Model):
    userId = models.IntegerField()
    postId = models.IntegerField(blank=True)#не обязательно к заполнению, заполняется автоматически в бэке
    bookId = models.IntegerField(blank=True)#не обязательно к заполнению, заполняется автоматически в бэке
