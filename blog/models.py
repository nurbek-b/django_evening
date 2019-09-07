from datetime import datetime
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',
                               on_delete=models.CASCADE)
    body = models.TextField()
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    date = models.DateTimeField(auto_now=datetime.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])