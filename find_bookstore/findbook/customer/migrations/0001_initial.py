# Generated by Django 3.0.4 on 2020-10-28 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=50)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('img', models.CharField(max_length=300, null=True)),
                ('publisher', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]
