from django.shortcuts import render
from .models import Feedback
from .forms import FeedbackForm
from django.views.generic import (
    CreateView,
)


def index(request):
    return render(request, 'base.html', context={})


class FeedbackCreate(CreateView):
    template_name = 'other/contacts.html'
    model = Feedback
    form_class = FeedbackForm
