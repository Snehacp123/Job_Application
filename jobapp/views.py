from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from jobapp.models import JobApplication
from jobapp.forms import JobapplicationForm
from django.contrib import messages


# Create a new job application.
class Applicant_Create_View(CreateView):
    model = JobApplication
    template_name = "applicant_add.html"
    form_class = JobapplicationForm
    success_url = reverse_lazy("home")

    # If the form is valid, save it and redirect to the success URL
    def form_valid(self, form):
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            form.instance.first_name = first_name.capitalize()
            form.save()
            messages.success(self.request, "Application submitted successfully.")
            return redirect(self.success_url)

    # If the form is invalid, show errors and redirect back to the create view
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return redirect("create")


# List all job applications.
class Applicants_List_View(ListView):
    model = JobApplication
    template_name = "applicants_list.html"

    def get(self, request):
        # Get all job applications and order them by descending ID.
        applicants = JobApplication.objects.all().order_by("-id")
        return render(request, self.template_name, {"applicants": applicants})


# Update a job application.
class Applicant_Update_View(UpdateView):
    model = JobApplication
    form_class = JobapplicationForm
    template_name = "applicant_edit.html"
    success_url = reverse_lazy("home")

    # If the form is valid, save it and redirect to the success URL
    def form_valid(self, form):
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            form.instance.first_name = first_name.capitalize()
            form.save()
            messages.success(self.request, "Application Updated successfully.")
            return redirect(self.success_url)

    # If the form is invalid, show errors and redirect back to the create view
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return redirect("create")


# Delete a job application.
class Applicant_Delete_View(DeleteView):
    model = JobApplication
    # Ask confirmation before Delete the application.
    template_name = "confirm_applicant_delete.html"
    success_url = reverse_lazy("home")
