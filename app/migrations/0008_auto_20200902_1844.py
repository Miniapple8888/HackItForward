# Generated by Django 3.1 on 2020-09-02 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200830_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasksubmission',
            name='task',
        ),
        migrations.RemoveField(
            model_name='tasksubmission',
            name='user',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='TaskSubmission',
        ),
    ]