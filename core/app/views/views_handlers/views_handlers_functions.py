from django.contrib.auth import get_user_model
from django.core.mail import send_mail

import base64


def is_email_unique(request, email: str):
    user_model = get_user_model()

    if user_model.objects.filter(email=email).count() == 0:
        return False
    else:
        request.session['errormessage_emailnotunique'] = True

        return True


def send_verification_mail(email, password):
    send_mail(subject='Social-Network Verify',

              message='''Hello, thank you for your interest in the project.

                            To verify your account, follow the link:
                            http://192.168.1.22:8000/handle/verify/{}/{}

                              '''.format(base64.b64encode(email.encode('ascii')).decode('ascii'),
                                         base64.b64encode(password.encode('ascii')).decode('ascii')),

              from_email='social-network@django.project', recipient_list=[email])
