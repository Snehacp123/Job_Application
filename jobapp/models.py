from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
import re
from datetime import date
from datetime import datetime

"""
    Represents a job application submitted by a candidate.
    Attributes :
        name, 
        phone number,
        email,
        date of birth,
        jobrole,
        qualification,
        experience,
        address
    Methods :
        __str__() :Returns a string representation of the job application.

"""


class JobApplication(models.Model):
    # validate the firstname
    def validate_firstname(firstname):
        nameregex = r"^[A-Za-z]+( [A-Za-z]+)?( [A-Za-z]+)?$"
        matchs = re.match(nameregex, firstname)
        if (
            (firstname == "")
            or (firstname is None)
            or (matchs is None)
            or (len(firstname) <= 3)
            or (len(firstname) >= 25)
        ):
            raise ValidationError(f"{firstname} is invalid")

    # validates the phone number
    def validate_phonenumber(phonenumber):
        phonepattern = r"^\d{10}$"
        matchs = re.match(phonepattern, phonenumber)
        if (phonenumber == "") or (matchs is None):
            raise ValidationError(f"{phonenumber} is invalid")

    # validates the date of birth
    def validate_dob(dob):
        today = date.today()

        time_diff = (today - dob).days / 365.25
        if dob == "" or dob == None or int(time_diff) < 18:
            raise ValidationError(
                "invalid date of birth , age must be minimum 18 years old"
            )

    first_name = models.CharField(
        max_length=25, null=False, validators=[validate_firstname]
    )
    last_name = models.CharField(max_length=25, null=True, blank=True)
    Country_choice = [("india", "+91"), ("canada", "+1")]
    country_code = models.CharField(
        max_length=20, choices=Country_choice, default="+91", null=False
    )
    phone_no = models.CharField(
        max_length=10, null=False, validators=[validate_phonenumber]
    )
    email = models.EmailField(max_length=50, unique=True, null=False)
    date_of_birth = models.DateField(null=False, validators=[validate_dob])
    Gender_choices = [("Male", "Male"), ("Female", "Female"), ("Other", "Other")]

    gender = models.CharField(
        max_length=6, choices=Gender_choices, default="Male", null=True
    )
    Jobrole_choices = [
        ("", "Choose a Job Role"),
        ("Frontend Developer", "Frontend Developer"),
        ("Backend Developer", "Backend Developer"),
        ("Fullstack Developer", "Fullstack Developer"),
        ("DevOps Engineer", "DevOps Engineer"),
        ("Ui/UX Designer", "Ui/UX Designer"),
    ]
    job_role = models.CharField(max_length=19, choices=Jobrole_choices, null=False)
    Qualification_choices = [
        ("", "Choose a Course"),
        ("BCA", "BCA"),
        ("Btech", "Btech"),
        ("MCA", "MCA"),
        ("MTech", "Mtech"),
    ]
    qualification = models.CharField(
        max_length=5, choices=Qualification_choices, null=False
    )
    Experience_year_choices = [
        ("", "Years"),
        ("fresher", "fresher"),
        ("1year", "1 year"),
        ("2year", "2 year"),
        ("3year", "3 year"),
        ("4plusyear", "4+ year"),
    ]
    experience_year = models.CharField(
        max_length=9, choices=Experience_year_choices, null=False
    )
    Experience_month_choices = [
        ("", "Months"),
        ("0month", "0 month"),
        ("1month", "1 month"),
        ("2month", "2 month"),
        ("3month", "3 month"),
        ("4month", "4 month"),
        ("5month", "5 month"),
    ]
    experience_month = models.CharField(
        max_length=6, choices=Experience_month_choices, null=False
    )
    address = models.CharField(max_length=100, null=True, blank=True)
    streetname = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=40, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    zipcode = models.TextField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.first_name
