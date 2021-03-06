# Generated by Django 3.1.1 on 2020-11-11 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testgateway', '0004_auto_20201111_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertestprofile',
            name='questions',
            field=models.ManyToManyField(blank=True, to='testgateway.Questions'),
        ),
        migrations.AlterField(
            model_name='usertestprofile',
            name='submitAnswer',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
