from django.db import models

from membership.models import Membership

# Create your models here.


class Plans(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    allowed_memberships = models.ManyToManyField(Membership)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    plans = models.ForeignKey(Plans, on_delete=models.CASCADE, null=True)
    postion = models.IntegerField()
    training_url = models.CharField(max_length=200)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title
