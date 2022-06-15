# Generated by Django 4.0.4 on 2022-06-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('p_id', models.IntegerField(null=True)),
                ('p_name', models.CharField(max_length=100, null=True)),
                ('c_name', models.CharField(max_length=100, null=True)),
                ('c_mail', models.CharField(max_length=100, null=True)),
                ('init_date', models.DateField(null=True)),
                ('ect', models.DateField(null=True)),
                ('status', models.CharField(choices=[('Inititated', 'Inititated'), ('Paused', 'Paused'), ('In progress', 'In progress'), ('Aborted', 'Aborted'), ('Completed', 'Completed')], max_length=200, null=True)),
                ('collabs', models.IntegerField(null=True)),
                ('phase', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], null=True)),
            ],
        ),
    ]