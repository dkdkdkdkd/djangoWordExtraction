from django.db import models

# Create your models here.

class WordDb(models.Model):
    eng = models.CharField(max_length=50)
    kor = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.eng}:{self.kor}'

