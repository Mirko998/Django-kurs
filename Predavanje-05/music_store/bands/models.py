from django.db import models

# Create your models here.
class Band(models.Model):
    """A model of a rock band."""
    name = models.CharField(max_length=200)
    can_rock = models.BooleanField(default=True)
    image = models.URLField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWtn4VAG1j1mzMFukZ4KFbAqxirEvDTqdMjA&usqp=CAU')
    description = models.CharField(max_length=500, default='')

    def __str__(self):
        return f'{self.name}'


class Member(models.Model):
    """A model of a rock band member."""
    name = models.CharField("Member's name", max_length=200)
    instrument = models.CharField(choices=(
            ('g', "Guitar"),
            ('b', "Bass"),
            ('d', "Drums"),
        ),
        max_length=1
    )
    band = models.ForeignKey("Band", on_delete=models.DO_NOTHING)

    def __str__(self):
        """" String representation of band member """
        translator = {
            'g': "Guitar",
            'b': "Bass",
            'd': "Drums"
        } 
        return f'{self.name}, {translator[self.instrument]}'