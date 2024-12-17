# Generated by Django 4.1 on 2024-12-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]