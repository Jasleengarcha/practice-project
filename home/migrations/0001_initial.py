# Generated by Django 4.1.3 on 2022-12-03 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('contact_no', models.CharField(max_length=15)),
                ('email_id', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField(null=True)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_mobile', models.CharField(max_length=15)),
                ('user_dob', models.DateField()),
                ('user_gender', models.CharField(max_length=10)),
                ('user_myfile', models.ImageField(upload_to='file_images/')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]