from django.db import models
from django.urls import reverse

from membership.models import Membership

# Create your models here.


class Plans(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    plan_thumbnail = models.ImageField(blank=True, null=True)
    allowed_memberships = models.ManyToManyField(Membership)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('plans:detail', kwargs={'slug': self.slug})

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')


class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    plans = models.ForeignKey(Plans, on_delete=models.CASCADE, null=True)
    postion = models.IntegerField()
    training_url = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('plans:lesson-detail', kwargs={
            'plan_slug': self.plan.slug,
            'lesson_slug': self.slug
        })
