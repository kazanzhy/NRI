# Generated by Django 2.1 on 2018-08-04 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='phone',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
    ]