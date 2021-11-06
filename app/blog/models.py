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


class Comment(models.Model):
    """ Comment for note """
    RATINGS = (
        (0, 'No score'),
        (1, 'Terrible'),
        (2, 'Bad'),
        (3, 'Normal'),
        (4, 'Good'),
        (5, 'Well done'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, related_name='comments', on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=True, verbose_name='Editing time')
    message = models.TextField(default='', blank=True, verbose_name='Comment')
    rating = models.IntegerField(default=0, choices=RATINGS, verbose_name='Score')

    def __str__(self):
        # https://django.fun/docs/django/ru/3.1/ref/models/instances/#django.db.models.Model.get_FOO_display
        return f'{self.get_rating_display()}: {self.message or "No comments"}'
