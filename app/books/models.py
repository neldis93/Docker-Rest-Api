# indicates the date of creation and the date of modification
from model_utils.models import TimeStampedModel
from django.db import models

class Books(TimeStampedModel):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    length = models.IntegerField()
    price = models.FloatField()

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['id']

    def __str__(self):
        return str(self.id) + '-' + self.title

