# Generated by Django 4.0.4 on 2022-04-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAndPlan', '0003_alter_plan_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='data',
            field=models.CharField(max_length=5),
        ),
    ]
