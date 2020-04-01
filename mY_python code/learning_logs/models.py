from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:  # хранит доп.информацию о модели
        verbose_name_plural = 'entries'  # иначе будет писать 'entrys' при обращении более чем к одной записи)

    def __str__(self):
        if len(self.text) < 50:
            return self.text
        else:
            return self.text + '...'


