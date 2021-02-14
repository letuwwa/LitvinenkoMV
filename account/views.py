from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ProfileForm, UserRegistrationForm


@login_required
def user_page(request):
    return render(request, 'account/user_page.html', {'section': 'user_page'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            p_form = profile_form.save(commit=False)
            p_form.user = new_user
            new_user.save()
            p_form.save()
            return render(request, 'account/register_done.html', {'new_user': new_user, 'new_profile': p_form})
    else:
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
    return render(request, 'account/register.html', {'user_form': user_form, 'profile_form': profile_form})
