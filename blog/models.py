from django.db import models
from django.conf import settings
from slugify import slugify

class Post(models.Model):
    name=models.CharField(max_length=60,null=True)
    field = models.CharField(max_length=25,null=True)
    title=models.CharField(max_length=500)
    content=models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)
    url= models.SlugField(max_length=500, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.url= slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
