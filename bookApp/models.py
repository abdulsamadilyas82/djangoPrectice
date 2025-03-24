from django.db import models
from django.db.models import CharField, DateField


# Book Model Class
class Books(models.Model):
    title = CharField(max_length=30)
    author = CharField(max_length=20)
    published_date = DateField(default=None)
    isbn = CharField(max_length=15, unique=True)