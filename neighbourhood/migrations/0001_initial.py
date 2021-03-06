# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-14 08:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(choices=[('Nasra Gardens ', 'Nasra Gardens'), ('Lucky summer', 'Lucky summer'), ('Westlands', 'Westlands'), ('Donholm', 'Donholm'), ('Umoja', 'Umoja'), ('Imara Daima', 'Imara Daima'), ('Kiambu', 'Kiambu'), ('Buruburu', 'Buruburu'), ('Gigiri', 'Gigiri'), ('Komarock', 'Komarock'), ('Highrise', 'Highrise'), ('Rongai', 'Rongai'), ('Karen', 'Karen'), ('Ruiru', 'Ruiru'), ('Roysambu', 'Roysambu'), ('Juja', 'Juja')], max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('police_dept', models.IntegerField(default='0722445233')),
                ('health_dept', models.IntegerField(default='0700505221')),
            ],
            options={
                'ordering': ['posted_on'],
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('post', models.TextField()),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Neighbourhood')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('hood', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Neighbourhood')),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='join',
            name='hood_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Neighbourhood'),
        ),
        migrations.AddField(
            model_name='join',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Posts'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.Neighbourhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
