# Generated by Django 3.1.7 on 2021-05-11 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210511_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_global',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.categoryglobal', verbose_name='Категория глобальная'),
        ),
    ]
