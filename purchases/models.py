from django.db import models
from django.contrib.auth.models import User


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    last_purchase_date = models.DateTimeField(null=True, blank=True)
    time_since_last_purchase = models.DurationField(null=True, blank=True)
    result = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.item
