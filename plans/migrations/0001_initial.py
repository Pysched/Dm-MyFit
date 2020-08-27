# Generated by Django 3.0.8 on 2020-08-27 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membership', '0002_auto_20200827_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('allowed_memberships', models.ManyToManyField(to='membership.Membership')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('title', models.CharField(max_length=120)),
                ('postion', models.IntegerField()),
                ('training_url', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('plans', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plans.Plans')),
            ],
        ),
    ]
