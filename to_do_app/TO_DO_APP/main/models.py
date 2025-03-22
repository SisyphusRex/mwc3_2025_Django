from django.db import models


class Todo(models.Model):
    """todo class"""

    item_name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()

    def __str__(self):
        """string method"""
        return str(self.item_name)
