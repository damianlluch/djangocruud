from django.db import models
from django.urls import reverse
from django.conf import settings

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    note = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(null=True)
    tag = models.CharField(max_length=128, default='untitled')
    task = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('books_fbv_user:book_edit', kwargs={'pk': self.pk})