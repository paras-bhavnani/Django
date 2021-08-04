#from blog.views import blogs
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    author_bio = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, default=None, on_delete=models.SET_NULL, null=True)
    class Meta:
        ordering = ['-date']


