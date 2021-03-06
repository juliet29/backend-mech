# Generated by Django 2.2.3 on 2019-07-30 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mech_app', '0002_remove_servicerequest_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicerequest',
            name='status',
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='plant',
            field=models.CharField(default='Mudor', max_length=20),
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
