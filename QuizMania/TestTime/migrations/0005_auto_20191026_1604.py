# Generated by Django 2.2.6 on 2019-10-26 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestTime', '0004_auto_20191026_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aws_b',
            name='Answer',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='aws_b',
            name='Option1',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='aws_b',
            name='Option2',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='aws_b',
            name='Option3',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='aws_b',
            name='Option4',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='aws_b',
            name='Question',
            field=models.CharField(max_length=1000),
        ),
    ]
