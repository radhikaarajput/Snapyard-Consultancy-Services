# Generated by Django 3.2.4 on 2021-06-29 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('subcategory', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('image', models.CharField(blank=True, max_length=5000, null=True)),
            ],
        ),
    ]