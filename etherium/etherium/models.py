from django.db import models

class User(models.Model):
    username=models.CharField(max_length=40)


class Item(models.Model):
    price=models.DecimalField(decimal_places=2,max_digits=10)
    name=models.CharField(max_length=40)
    availablenum=models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
