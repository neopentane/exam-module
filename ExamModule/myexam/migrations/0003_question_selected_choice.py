# Generated by Django 2.1.7 on 2019-04-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myexam', '0002_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='selected_choice',
            field=models.IntegerField(default=1),
        ),
    ]