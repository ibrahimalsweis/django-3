# Generated by Django 4.0.4 on 2022-04-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_categorys_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorys',
            name='name',
            field=models.CharField(max_length=5),
        ),
    ]
