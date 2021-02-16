from django import forms
from .models import Feedback, JobModel


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'text', 'email')


class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = '__all__'
        labels = {
            "job_location": "Job Location",
            "published_on": "Publish Date"
        }