from django.db import models
from membership.models import Membership

# Create your models here.


class Plan(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    allowed_memberships = models.ManyToManyField(Membership)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
