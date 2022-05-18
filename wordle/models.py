from django.db import models

# Create your models here.
class WordleModel(models.Model):
    wordle = models.CharField(max_length=5, unique=True, null=False)

    def __str__(self) -> str:
        return self.wordle

    def length(self) -> int:
        return len(self.wordle)