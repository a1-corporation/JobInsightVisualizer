# Generated by Django 5.1.2 on 2024-10-16 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobMarket', '0002_delete_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostingByJobPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('collected_on', models.DateTimeField(verbose_name='데이터 수집 일자')),
                ('job_sub_type_name', models.CharField(max_length=100, verbose_name='하위 직군 이름')),
                ('count', models.IntegerField(verbose_name='공고 수')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
