from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
import uuid

from django.db.models import SET_NULL
from django.urls import reverse
from datetime import datetime

# Create your models here.
# User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    number = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='profile.jpg')
    location = models.CharField(max_length=100, blank=True)
    # username = models.CharField(max_length=100)

    def __str__(self):
        # return self.name
        return self.user.username


class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.user.username



class ChatMessage(models.Model):
    body = models.TextField()
    msg_sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="msg_sender")
    msg_receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="msg_receiver")
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.body


class Post(models.Model):
    # user = models.CharField(max_length=100)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)
    # username = models.CharField(max_length=100)

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.id})

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    # user = models.CharField(max_length=100)
    # username = models.CharField(max_length=100)


    def __str__(self):
        return self.user


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    commenter_name = models.CharField(max_length=200)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    # username = models.CharField(max_length=100)

    def __str__(self):
        return self.user
        # return '%s - %s' % (self.comment_body, self.commenter_name)
