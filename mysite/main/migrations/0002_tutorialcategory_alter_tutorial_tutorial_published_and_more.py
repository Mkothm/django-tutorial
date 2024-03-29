# Generated by Django 4.2.3 on 2023-07-25 11:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorialCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_category', models.CharField(max_length=200)),
                ('category_summary', models.CharField(max_length=200)),
                ('category_slug', models.CharField(default=1, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateField(default=datetime.datetime(2023, 7, 25, 11, 0, 15, 133814), verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='TutorialSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_series', models.CharField(max_length=200)),
                ('series_summary', models.CharField(max_length=200)),
                ('tutorial_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.tutorialcategory', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
    ]
