from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=300 , default='1')
    image = models.ImageField(null = True)
    body = models.TextField()
    pubdate = models.DateTimeField(default = datetime.now())
    def __str__(self):
        return self.name

    def summary(self):
        return self.body[:300]

    def pub_date_pretty(self):
        return self.pubdate.strftime(' %b %e %Y ')

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default = None)
    post_related = models.ForeignKey(Post, on_delete=models.CASCADE , default = None)
    body = models.TextField()
    upvotes = models.IntegerField()
    def __str__(self):
        return self.body

class votes(models.Model):
    who = models.ForeignKey(User , on_delete=models.CASCADE)
    related_comment = models.ForeignKey(Comments , on_delete=models.CASCADE)



