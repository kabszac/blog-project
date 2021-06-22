from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 100)
    #unrestricted field content
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    # on_delete deletes a post or a user with his post
    author = models.ForeignKey(User, on_delete = models.CASCADE)


    def  __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs = {"pk":self.pk})


