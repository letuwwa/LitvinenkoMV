from django import forms
from .models import Feedback, JobModel, JobApplyModel


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


class JobModelForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = '__all__'


class ApplyEmployeeForm(forms.ModelForm):
    job = forms.ModelChoiceField(queryset=JobModel.objects.all(), empty_label=None, label='Вакансия', disabled=True)

    class Meta:
        model = JobApplyModel
        fields = ('apply_request', 'job')


class ApplyEmployerForm(forms.ModelForm):
    class Meta:
        model = JobApplyModel
        fields = ('job', 'apply_response', 'status')
