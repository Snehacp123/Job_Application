from django.urls import path

# This line imports the `views` module from the `jobapp` application. This module contains the view functions that will be handled by the URL patterns.
from jobapp import views

urlpatterns = [
    # This URL pattern maps to the `Applicants_List_View` view class.
    path("", views.Applicants_List_View.as_view(), name="home"),
    # This URL pattern maps to the `Applicant_Create_View` view class.
    path("create/", views.Applicant_Create_View.as_view(), name="create"),
    # The `<pk>` placeholder will be replaced with the primary key of the applicant to be updated. It maps to the `Applicant_Update_View` view class
    path("update/<pk>/", views.Applicant_Update_View.as_view(), name="update"),
    # The `<pk>` placeholder will be replaced with the primary key of the applicant to be deleted. It maps to the `Applicant_Delete_View` view class
    path("delete/<pk>/", views.Applicant_Delete_View.as_view(), name="delete"),
]
