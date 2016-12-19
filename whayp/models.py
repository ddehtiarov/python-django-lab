from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


class Post(models.Model):
    user = models.ForeignKey(User, default=1)
    description = models.CharField(max_length=250, default='')
    pub_date = models.DateTimeField(default=datetime.now())
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user) + ' - ' + self.description


class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    photo_file = models.FileField()
    is_favorite = models.BooleanField(default=False)
    is_main = models.BooleanField(default=False)
