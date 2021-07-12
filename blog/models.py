from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200) #charfield is for smaller titles like name ex: title of the blog
    author = models.ForeignKey( #foreign key is a key share in two table that might be named differantly
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    smallbody = str(body)[0:200]
    def __str__(self):
        return self.title

    def get_absolute_url(self):  # new
        return reverse('post_detail', args=[str(self.id)])