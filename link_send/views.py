from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.conf import settings



from django.core.mail import send_mail



from link_send.forms import EmailForm
from link_send.tokens import account_activation_token

def home(request):
    return render(request, 'home.html')

def email_user(subject,body,to_email,from_email=settings.EMAIL_HOST_USER):
   """ Common Function for emailing user """
   send_mail(subject, body, from_email, [to_email])


def send_mail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.is_active = False
            email.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': (user.pk),
                'token': account_activation_token.make_token(user),
            })
            email_user(subject, message,user.email)

            return redirect('link_sent')
    else:
        form = EmailForm()
    return render(request, 'form.html', {'form': form})




def link_sent(request):
    return render(request, 'link_sent.html')


def activate(request, uidb64, token):
    print(str(uidb64))
    print('I am printing ')
    try:
        # print("I am also printing")
        uid = uidb64
        print(uid)
        user = User.objects.get(pk=uidb64)
        print(user)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('form')
    else:
        return render(request, 'invalid.html')

