from django.db import models


class Sample(models.Model):
    attachment = models.FileField()

    def __str__(self):
        return f"<Sample - {self.id}>"
