from django import forms
from .models import JobApplication

"""
    Form for creating a new job application.
    This form is used to collect information from job applicants.

"""


class JobapplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = "__all__"
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "country_code": "Contact",
            "phone_no": "Contact",
            "email": "Email",
            "date_of_birth": "Date of Birth",
            "gender": "Gender",
            "qualification": " Qualification",
            "job_role": "Job Role",
            "experience_year": "Select Job Experience(in years)",
            "experience_month": "Select Job Experience(in months)",
            "address": "Address",
            "streetname": "Street Nmae",
            "state": "State",
            "city": "City",
            "country": "Country",
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "input",
                    "id": "firstname",
                    "placeholder": "Enter First Name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "input",
                    "id": "lastname",
                    "placeholder": "Enter Last Name",
                }
            ),
            "country_code": forms.Select(
                attrs={
                    "class": "selectopt",
                    "id": "code",
                }
            ),
            "phone_no": forms.TextInput(
                attrs={
                    "class": "inputs",
                    "id": "mob",
                    "placeholder": "Enter Phone Number",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "input",
                    "id": "email",
                    "placeholder": "Enter Email",
                }
            ),
            "date_of_birth": forms.DateInput(
                attrs={
                    "class": "input",
                    "type": "date",
                    "id": "dob",
                    "placeholder": "Enter Date of Birth",
                }
            ),
            "gender": forms.RadioSelect(
                attrs={
                    "class": "radiotab",
                }
            ),
            "qualification": forms.Select(
                attrs={
                    "class": "selectopt",
                    "id": "qualification",
                }
            ),
            "job_role": forms.Select(
                attrs={
                    "id": "Job-role",
                    "class": "selectopt",
                }
            ),
            "experience_year": forms.Select(
                attrs={
                    "id": "selectyearopt",
                    "class": "selectopt",
                }
            ),
            "experience_month": forms.Select(
                attrs={
                    "id": "selectmonthopt",
                    "class": "selectopt",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "input",
                    "id": "address",
                    "placeholder": "Enter Address",
                }
            ),
            "streetname": forms.TextInput(
                attrs={
                    "class": "input",
                    "id": "streetname",
                    "placeholder": "Enter Street Name",
                }
            ),
            "city": forms.TextInput(
                attrs={
                    "class": "input",
                    "id": "city",
                    "placeholder": "Enter City",
                }
            ),
            "state": forms.TextInput(
                attrs={
                    "class": "input",
                    "id": "state",
                    "placeholder": "Enter State",
                }
            ),
            "country": forms.TextInput(
                attrs={
                    "class": "input",
                    "id": "country",
                    "placeholder": "Enter Country",
                }
            ),
            "zipcode": forms.TextInput(
                attrs={
                    "class": "input",
                    "id": "zipcode",
                    "placeholder": "Enter Zipcode",
                }
            ),
        }
