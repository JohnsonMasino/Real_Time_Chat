# Generated by Django 5.0.1 on 2024-01-28 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='Johnson Masino', max_length=1000),
        ),
    ]