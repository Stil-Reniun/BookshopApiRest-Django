from django.db import models

class Genre (models.Model):
    title = models.CharField(max_length=25)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
