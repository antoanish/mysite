# Generated by Django 2.2 on 2019-04-08 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
                ('image', models.ImageField(default='default.jpg', upload_to='post_img')),
            ],
        ),
    ]
