# Generated by Django 4.2.11 on 2024-04-13 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuw', '0009_alter_contact_availability_alter_contact_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
