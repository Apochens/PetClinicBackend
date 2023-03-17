# Generated by Django 4.1.7 on 2023-03-17 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_delete_role_alter_department_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('tag', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
