from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)                    #max_length is required, CharField is varchar in database
    date_created = models.DateTimeField(default=datetime.now)
    date_updated = models.DateTimeField(null=True, blank=True)
    content = models.TextField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'Title: {}'.format(self.title)

class Comment(models.Model):                                     #classes should be separated with a new line for readability
    date_created = models.DateTimeField(default=datetime.now)
    cois_acntent = models.TextField(max_length=200)
    post = models.ForeignKey(Post,
                on_delete=models.CASCADE,                       #on_delete is constant
                related_name='comments',
                null=True, blank=True)
