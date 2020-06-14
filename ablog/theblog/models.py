from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Codingfan")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author) + ' | ' + self.title_tag

    def get_absolute_url(self):
        return reverse('home')
        # return reverse("article-detail", kwargs={"pk": self.pk})
