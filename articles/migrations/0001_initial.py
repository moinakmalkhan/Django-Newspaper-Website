# Generated by Django 3.1.4 on 2020-12-12 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.profilesettings')),
            ],
        ),
        migrations.CreateModel(
            name='FavCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.profilesettings')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('reply', models.ManyToManyField(blank=True, related_name='comment_reply', to='articles.Reply')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.profilesettings')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.category')),
                ('comments', models.ManyToManyField(blank=True, to='articles.Comment')),
                ('likes', models.ManyToManyField(blank=True, to='registration.ProfileSettings')),
            ],
        ),
    ]