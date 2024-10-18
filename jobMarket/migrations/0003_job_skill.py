from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('jobMarket', '0002_delete_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobNeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('job_name', models.CharField(max_length=100, verbose_name='하위 직군 이름')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('experience_level', models.CharField(max_length=100, verbose_name='필요 경력 수준')),
                ('skill', models.CharField(max_length=100, verbose_name='기술명')),
                ('percentage', models.CharField(max_length=100, verbose_name='백분율')),
                ('job_need', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='skills', to='jobMarket.JobNeed', verbose_name='기술 요구 직군')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]