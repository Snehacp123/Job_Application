# Generated by Django 4.2.5 on 2023-10-22 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0006_alter_jobapplication_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='country',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='country_code',
            field=models.CharField(blank=True, choices=[('', '+91'), ('india', '+91'), ('canada', '+1')], default='+91', max_length=20),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='last_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='state',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='streetname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='zipcode',
            field=models.TextField(blank=True, max_length=6, null=True),
        ),
    ]
