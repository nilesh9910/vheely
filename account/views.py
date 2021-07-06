from django.shortcuts import redirect, render
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .token import account_activation_token
# Create your views here.
from .forms import RegistrationForm, UserEditForm

from .models import UserBase

@login_required
def dashboard(request):
    return render(request, 'account/user/dashboard.html')

def account_register(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            # Setup Email
            current_site = get_current_site(request)
            subject = 'Activate your account'
            message = render_to_string('account/registration/account_activation_email.html', {
                'user': user, 
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token' : account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse("You are register succesfully. Please check your email to activate your account")
    else:
        registerForm = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form': registerForm})

def account_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user =  UserBase.objects.get(pk=uid)
    except():
        pass
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account:dashboard')
    else:
        return render(request, 'account/registration/activation_invalid.html')

@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request, 'account/user/edit_details.html', {'user_form': user_form})