from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=128, verbose_name="Title")
    message = models.TextField(default="", verbose_name="Text")
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="Creation time")
    public = models.BooleanField(default=False, verbose_name="Post")
    author = models.ForeignKey(User, related_name="authors", on_delete=models.PROTECT)

    def __str__(self):
        return self.title
