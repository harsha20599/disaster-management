# Generated by Django 3.0.3 on 2020-03-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='givealert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alertinfo', models.CharField(default='testing', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='testing', max_length=100)),
                ('answer', models.CharField(default='testing', max_length=100)),
                ('username', models.CharField(default='null', max_length=200)),
                ('password', models.CharField(default='null', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourlocation', models.CharField(default='null', max_length=200)),
                ('safeplacesname', models.CharField(default='kkd', max_length=200)),
                ('safeplacesdistance', models.IntegerField(default='23')),
                ('safeplacescapacity', models.IntegerField(default='200')),
                ('safeplacescontact', models.IntegerField(default='5679')),
                ('transportname', models.CharField(default='orange travels', max_length=200)),
                ('transporttypeof', models.CharField(default='bus', max_length=200)),
                ('transportcontact', models.IntegerField(default='5679')),
                ('rescueteamtype', models.CharField(default='navy', max_length=200)),
                ('rescueteammembers', models.IntegerField(default='5')),
                ('rescuecontact', models.IntegerField(default='420420')),
            ],
        ),
    ]