# Generated by Django 5.1.2 on 2024-10-17 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobMarket', '0002_delete_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartFour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('language', models.CharField(max_length=50, verbose_name='언어')),
                ('role', models.CharField(max_length=50, verbose_name='직무')),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='비율')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
