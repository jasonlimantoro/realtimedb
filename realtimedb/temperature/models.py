from django.db import models


class Temperature(models.Model):
    DATETIME_FORMAT = '%b %d %Y, %H:%M:%S'
    value = models.FloatField()
    location = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"({self.value}, {self.location})"

    def detail_updated_at(self):
        return self.updated_at.strftime(self.DATETIME_FORMAT)

    def detail_created_at(self):
        return self.created_at.strftime(self.DATETIME_FORMAT)
