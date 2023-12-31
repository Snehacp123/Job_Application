# Generated by Django 4.2.5 on 2023-10-22 05:43

from django.db import migrations, models
import jobapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0004_alter_jobapplication_country_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='country_code',
            field=models.CharField(choices=[('india', '+91'), ('canada', '+1')], default='+91', max_length=20),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='date_of_birth',
            field=models.DateField(validators=[jobapp.models.JobApplication.validate_dob]),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='experience_month',
            field=models.CharField(choices=[('', 'Months'), ('0month', '0 month'), ('1month', '1 month'), ('2month', '2 month'), ('3month', '3 month'), ('4month', '4 month'), ('5month', '5 month')], max_length=6),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='experience_year',
            field=models.CharField(choices=[('', 'Years'), ('fresher', 'fresher'), ('1year', '1 year'), ('2year', '2 year'), ('3year', '3 year'), ('4plusyear', '4+ year')], max_length=9),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='first_name',
            field=models.CharField(max_length=25, validators=[jobapp.models.JobApplication.validate_firstname]),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=6),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='job_role',
            field=models.CharField(choices=[('', 'Choose a Job Role'), ('Frontend Developer', 'Frontend Developer'), ('Backend Developer', 'Backend Developer'), ('Fullstack Developer', 'Fullstack Developer'), ('DevOps Engineer', 'DevOps Engineer'), ('Ui/UX Designer', 'Ui/UX Designer')], max_length=19),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='phone_no',
            field=models.CharField(max_length=10, unique=True, validators=[jobapp.models.JobApplication.validate_phonenumber]),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='qualification',
            field=models.CharField(choices=[('', 'Choose a Course'), ('BCA', 'BCA'), ('Btech', 'Btech'), ('MCA', 'MCA'), ('MTech', 'Mtech')], max_length=5),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='zipcode',
            field=models.TextField(max_length=6, null=True),
        ),
    ]
