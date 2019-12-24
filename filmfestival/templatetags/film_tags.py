import re
from django import template
from festival.models import Project
from filmfestival.models import Film

register = template.Library()




@register.simple_tag(takes_context=True)
def project_film_by_directors(context, **kwargs):
    projects = Project.objects.filter(**kwargs)
    context['films'] = Film.objects.filter(project__in=projects, status=Film.SELECTED).order_by('dir_by')
    return ''

@register.simple_tag(takes_context=True)
def project_film_by_title(context, **kwargs):
    projects = Project.objects.filter(**kwargs)
    context['films'] = Film.objects.filter(project__in=projects, status=Film.SELECTED).order_by('title')
    return ''

@register.simple_tag(takes_context=True)
def project_film_by_id(context, *ids):
    context['films'] = Film.objects.filter(id__in=ids, status=Film.SELECTED).order_by('title')
    return ''
