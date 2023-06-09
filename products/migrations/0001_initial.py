# Generated by Django 3.2 on 2023-03-20 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('format_type', models.CharField(choices=[('vertical', 'Vertical'), ('horizontal', 'Horizontal')], max_length=10)),
                ('image_path', models.CharField(max_length=255)),
                ('is_new_arrival', models.BooleanField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.artist')),
            ],
        ),
    ]
