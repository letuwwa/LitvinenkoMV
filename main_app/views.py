from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Feedback
from .forms import FeedbackForm
from django.views.generic import (
    CreateView,
)


def index(request):
    return render(request, 'base.html', context={})


def feedback_response(request):
    return render(request, 'other/contacts_response_success.html', context={})


class FeedbackCreate(CreateView):
    template_name = 'other/contacts.html'
    model = Feedback
    form_class = FeedbackForm

    def get_success_url(self):
        return reverse_lazy('contacts_r')
