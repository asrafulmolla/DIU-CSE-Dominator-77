# Generated by Django 4.2.4 on 2024-07-13 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_home_about_img_alter_home_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='instagram',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='student_ID',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
