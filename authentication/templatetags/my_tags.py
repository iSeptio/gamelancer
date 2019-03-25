from django import template
from django.contrib.auth.forms import AuthenticationForm
register = template.Library()


@register.inclusion_tag("tags/login.html", takes_context=True)
def login_form(context):
    return {
        'form': AuthenticationForm,
    }


@register.inclusion_tag("tags/logout.html", takes_context=True)
def logout_tag(context):
    return {}
