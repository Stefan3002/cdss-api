# Generated by Django 5.2 on 2025-04-29 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('downloads', models.IntegerField(default=0)),
                ('publishDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
