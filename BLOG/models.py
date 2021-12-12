from django.db import models
from django.urls import reverse
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=400)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title[:40]

    # return url for detailview with specefied index that is like detail/id
    def get_absolute_url(self):  # new
        return reverse('detailview', args=[str(self.id)])
