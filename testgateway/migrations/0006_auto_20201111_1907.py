# Generated by Django 3.1.1 on 2020-11-11 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testgateway', '0005_auto_20201111_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Userstats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitAnswer', models.CharField(blank=True, max_length=50)),
                ('time', models.TimeField(blank=True)),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testgateway.questions')),
                ('userProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testgateway.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='Usertestprofile',
        ),
        migrations.AddField(
            model_name='profile',
            name='userStat',
            field=models.ManyToManyField(through='testgateway.Userstats', to='testgateway.Questions'),
        ),
    ]