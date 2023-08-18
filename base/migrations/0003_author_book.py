# Generated by Django 4.2.1 on 2023-07-05 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_user_email_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('Age', models.IntegerField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publishDate', models.DateField()),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='base.author')),
            ],
        ),
    ]