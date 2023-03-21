from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=80)
    
    def __str__(self):
        return self.name


class Poster(models.Model):
    FORMAT_CHOICES = (
        ('vertical', 'Vertical'),
        ('horizontal', 'Horizontal'),
    )

    title = models.CharField(max_length=80)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    format_type = models.CharField(max_length=15, choices=FORMAT_CHOICES)
    image_path = models.ImageField(upload_to='posters/')
    is_new_arrival = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title