from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    status_choices=(
        ('draft','Draft'),
        ('published','Published')
    )
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    status=models.CharField(max_length=10,choices=status_choices,default='draft')

    class Meta:
        ordering=('-publish',)

    def __str__(self) -> str:
        return self.title
        