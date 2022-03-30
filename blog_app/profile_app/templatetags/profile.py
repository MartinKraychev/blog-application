from django import template

from blog_app.profile_app.models import Profile

register = template.Library()


@register.simple_tag(takes_context=True)
def get_profile(context):
    request = context['request']
    profile_id = request.user.id
    profile = Profile.objects.filter(pk=profile_id).first()
    return profile
