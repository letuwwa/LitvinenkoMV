from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import (
    Feedback,
    JobModel
)
from .forms import (
    FeedbackForm,
    JobListingForm,
)
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


def job_single(request, id):
    job_query = get_object_or_404(JobModel, id=id)
    context = {
        'q': job_query,
    }
    return render(request, "jobs/job_single.html", context)


@login_required
def job_listing(request):
    query = JobModel.objects.all().count()

    qs = JobModel.objects.all().order_by('-published_on')
    paginator = Paginator(qs, 5)  # Show 3 jobs per page
    page = request.GET.get('page')
    try:
        qs = paginator.page(page)
    except PageNotAnInteger:
        qs = paginator.page(1)
    except EmptyPage:
        qs = paginator.page(paginator.num_pages)

    context = {
        'query': qs,
        'job_qs': query
    }
    return render(request, "jobs/job_listing.html", context)


@login_required
def job_post(request):
    form = JobListingForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('/job_listing/')
    context = {
        'form': form,
    }
    return render(request, "jobs/job_post.html", context)
