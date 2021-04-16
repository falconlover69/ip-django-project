from django.db import models
from datetime import datetime
from django_mysql.models import ListCharField

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    by = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"

class Rating(models.Model): 
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __int__(self):
        return self.likes

    class Meta:
        verbose_name_plural = "Rating"
