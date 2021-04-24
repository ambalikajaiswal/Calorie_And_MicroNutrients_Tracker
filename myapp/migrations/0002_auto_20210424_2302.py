# Generated by Django 3.1.2 on 2021-04-24 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('carbs', models.FloatField()),
                ('protein', models.FloatField()),
                ('fats', models.FloatField()),
                ('calories', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Link',
        ),
    ]