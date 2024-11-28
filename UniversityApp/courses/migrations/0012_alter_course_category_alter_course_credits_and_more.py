# Generated by Django 4.2.16 on 2024-11-28 15:02

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_course_has_lector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('Web Design', 'Web Design'), ('Graphic Design', 'Graphic Design'), ('Video Editing', 'Video Editing'), ('Online Marketing', 'Online Marketing')], help_text='Course category: This field is required!', max_length=40),
        ),
        migrations.AlterField(
            model_name='course',
            name='credits',
            field=models.PositiveSmallIntegerField(default=1, help_text='Required field!', validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.PositiveSmallIntegerField(default=1, help_text='Required field!', validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(default=datetime.date(2024, 11, 28), help_text='Course starting date: This field is required!'),
        ),
    ]
