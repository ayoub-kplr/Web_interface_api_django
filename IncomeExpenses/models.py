from django.db import models


class IncomeExpenses(models.Model):
    type = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()


    def __str__(self):
        return self.category + " - " + self.type

