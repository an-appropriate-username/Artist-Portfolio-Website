# Generated by Django 4.2.11 on 2024-04-12 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kuw', '0005_remove_contact_over_delete_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='availability',
            field=models.TextField(default='', editable=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='questions',
            field=models.TextField(default='', editable=False),
        ),
    ]
