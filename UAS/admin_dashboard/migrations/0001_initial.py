# Generated by Django 5.1.6 on 2025-02-24 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_name', models.CharField(max_length=255, unique=True)),
                ('roles', models.ManyToManyField(blank=True, to='accounts.role')),
            ],
        ),
    ]
