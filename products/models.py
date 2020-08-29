from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    brand = models.CharField(
        max_length=254, null=True, blank=True)
    recommeded_for = models.CharField(
        max_length=254, null=True, blank=True)
    image_url = models.URLField(
        max_length=1024, null=True, blank=True)
    image = models.ImageField(
        null=True, blank=True)

    def averagereview(self):
        ratings = Comment.objects.filter(
                product=self).aggregate(average=Avg('rate'))
        avg = 0
        if ratings["average"] is not None:
            avg = float(ratings["average"])
        return avg

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=250, blank=True, null=False)
    comment = models.CharField(max_length=250, blank=True)
    Rating = (
        (0, 'No Rating'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    rate = models.IntegerField(choices=Rating, default=0)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
