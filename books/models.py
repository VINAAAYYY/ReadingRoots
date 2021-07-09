from django.db import models

# Create your models here.
class book(models.Model):
    book_id = models.AutoField
    book_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, default="")
    author = models.CharField(max_length = 20, default="")
    language = models.CharField(max_length=20)

    def __str__(self):
        return self.book_name