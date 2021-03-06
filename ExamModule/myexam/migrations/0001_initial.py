# Generated by Django 2.1.7 on 2019-03-31 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=50, verbose_name='Choice')),
                ('position', models.IntegerField(verbose_name='position')),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('question_no', models.IntegerField(verbose_name='question_no')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myexam.Exam')),
            ],
            options={
                'ordering': ('question_no',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_modules', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myexam.Modules')),
                ('roll_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myexam.Modules'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='myexam.Question'),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together={('exam', 'question'), ('exam', 'question_no')},
        ),
        migrations.AlterUniqueTogether(
            name='choice',
            unique_together={('question', 'choice'), ('question', 'position')},
        ),
    ]
