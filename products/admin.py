from django.contrib import admin
from .models import Poster, Artist

# Register your models here.


class PosterAdmin(admin.ModelAdmin):
    list_display = (
        'artist',
        'title',
        'format_type',
        'image_path',
        'is_new_arrival',
        'price',
    )


class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Poster, PosterAdmin)
