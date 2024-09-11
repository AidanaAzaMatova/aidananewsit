from django.db import models

class New(models.Model):
    new_text = models.CharField(max_length=200)

    def __str__(self):
        return self.new_text