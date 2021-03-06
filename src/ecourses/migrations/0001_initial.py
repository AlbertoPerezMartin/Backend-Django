# Generated by Django 3.0.3 on 2020-02-04 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('course_name', models.TextField()),
                ('course_approval_score', models.IntegerField()),
                ('course_description', models.TextField()),
                ('course_availability', models.BooleanField()),
            ],
        ),
    ]
