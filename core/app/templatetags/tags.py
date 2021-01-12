from django import template

from rest_framework.authtoken.models import Token

register = template.Library()


@register.simple_tag
def check_session_error_variables(request):
    session_error_variables_dict = {'errormessage_emailnotunique': 'The entered email address is already in use',
                                    'errormessage_signin_data_wrong': 'Invalid data entered',
                                    'errormessage_invalidverification': 'Confirmation link is invalid'}

    for error_variable in session_error_variables_dict:
        if request.session.get(error_variable, default=False):
            message = session_error_variables_dict[error_variable]

            del request.session[error_variable]

            return message


@register.simple_tag
def check_session_info_variables(request):
    session_info_variables_dict = {'infomessage_emailsent': 'A confirmation mail was sent to the entered email address',
                                   'infomessage_verified': 'You have successfully registered, log in.'}

    for info_variable in session_info_variables_dict:
        if request.session.get(info_variable, default=False):
            message = session_info_variables_dict[info_variable]

            del request.session[info_variable]

            return message


@register.simple_tag
def get_current_user_token(request):
    current_user_token = Token.objects.filter(user=request.user).first()

    return current_user_token
