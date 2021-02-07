from django.db import models

# Create your models here.

class Service(models.Model):
    name  = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.URLField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQif6kzNl9lDfDPn3rvrt_ZQykb0tU1ZU3KlA&usqp=CAU')
    price = models.IntegerField(default=0)


class FAQ(models.Model):
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=250)

#ORM SQL INJECTION