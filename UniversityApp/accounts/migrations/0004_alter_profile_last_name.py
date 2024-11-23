# Generated by Django 4.2.16 on 2024-11-23 14:39

import UniversityApp.validators.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(2), UniversityApp.validators.validators.AlphabeticValidator()]),
        ),
    ]
