# Generated by Django 2.1.3 on 2018-11-21 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date_of_birth',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
