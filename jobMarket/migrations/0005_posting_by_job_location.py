from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('jobMarket', '0004_merge_0003_chartfour_0003_job_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostingByJobLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('location_name', models.CharField(max_length=50, verbose_name='지역 이름')),
                ('experience_level', models.CharField(max_length=20, verbose_name='경력')),
                ('rate', models.FloatField(verbose_name='백분율')),
            ],
            options={
                'abstract': False,
            },
        )
    ]