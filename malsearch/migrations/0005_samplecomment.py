# Generated by Django 3.1.4 on 2020-12-07 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('malsearch', '0004_auto_20201207_0215'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='malsearch.sample')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
