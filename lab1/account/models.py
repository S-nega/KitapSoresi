from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    # birthdate = models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    birthdate = models.DateField(['%d-%m-%Y'])#???
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    info = models.TextField(blank=True)

    def __str__(self):
        return self.name