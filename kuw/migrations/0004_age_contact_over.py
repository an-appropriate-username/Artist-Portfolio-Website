# Generated by Django 4.2.11 on 2024-04-12 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kuw', '0003_rename_contactform_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='over',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kuw.age'),
        ),
    ]
