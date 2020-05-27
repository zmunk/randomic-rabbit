from django.db import models

class RandomNumber(models.Model):
    value = models.IntegerField(default=1)
    next_update_time = models.IntegerField(default=1)

    def __str__(self):
        return f"value: {self.value}, next update: {self.next_update_time}"
