from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone


class ValueArray(models.Model):
    created_date = models.DateTimeField(
            default=timezone.now)
    data_input = JSONField()
    data_output = JSONField()
    ip = models.CharField(max_length=15)

    def __str__(self):
        return self.created_date

