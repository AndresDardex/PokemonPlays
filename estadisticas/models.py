from django.db import models

class Pokemon(models.Model):
    Name = models.CharField(max_length=50)
    HP = models.IntegerField(null=True)
    Attack = models.IntegerField(null=True)
    Defense = models.IntegerField(null=True)
    Special_Attack = models.IntegerField(null=True)
    Special_Defense = models.IntegerField(null=True)
    Speed = models.IntegerField(null=True)
    Element = models.CharField(max_length=50, null=True)
