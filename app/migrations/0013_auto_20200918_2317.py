# Generated by Django 3.1 on 2020-09-19 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_tag_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='one_liner',
            field=models.CharField(default='', help_text='A one line description of the Challenge', max_length=50, verbose_name='One Line Description'),
        ),
        migrations.AddField(
            model_name='project',
            name='one_liner',
            field=models.CharField(default='', help_text='A one line description of the Challenge', max_length=50, verbose_name='One Line Description'),
        ),
    ]
