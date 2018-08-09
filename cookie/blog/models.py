from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('users.User', null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    creyt_d = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['published_date']


class Author(models.Model):
    name = models.CharField(max_length=200)
    create_by = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})
