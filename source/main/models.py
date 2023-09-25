from django.db import models


class Items(models.Model):
    item = models.CharField(max_length=1024)

    def __str__(self):
        return f"{self.item}"

    def __repr__(self):
        return f"{self.item}"
