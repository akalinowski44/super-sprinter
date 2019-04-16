# Generated by Django 2.1.7 on 2019-04-16 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(verbose_name='creation date')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_title', models.CharField(max_length=30)),
                ('user_story', models.TextField()),
                ('acceptance_criteria', models.TextField()),
                ('business_value', models.PositiveIntegerField(default=0)),
                ('estimation', models.PositiveIntegerField(default=0)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sprinter.Project')),
            ],
        ),
    ]
