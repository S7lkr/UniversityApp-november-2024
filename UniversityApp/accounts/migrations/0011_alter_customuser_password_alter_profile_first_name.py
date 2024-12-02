# Generated by Django 4.2.16 on 2024-12-01 21:03

import UniversityApp.validators.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_profile_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(8), UniversityApp.validators.PasswordLengthValidator()]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), UniversityApp.validators.AlphabeticValidator()]),
        ),
    ]
