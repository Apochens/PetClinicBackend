# Generated by Django 4.1.7 on 2023-03-05 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SingleChoiceQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('optionA', models.CharField(max_length=100)),
                ('optionB', models.CharField(max_length=100)),
                ('optionC', models.CharField(max_length=100)),
                ('optionD', models.CharField(max_length=100)),
                ('answer', models.CharField(choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D')], default=1, max_length=10)),
                ('disease_type', models.CharField(choices=[('infectious', '传染病'), ('parasitic', '寄生虫病'), ('internal', '内科'), ('obstetric', '外产科疾病'), ('surgery', '常用手术'), ('immunology', '免疫')], default='internal', max_length=20)),
                ('score', models.IntegerField(default=5)),
            ],
        ),
    ]