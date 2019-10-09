import re
from django import template

from festival.models import Artist, Project, Art

register = template.Library()


#
# @register.assignment_tag
# def artists(event, flags=0):
#     return Artist.objects.filter(event = event).order_by('name')


@register.simple_tag(takes_context=True)
def project_art(context, **kwargs):
    projects = Project.objects.filter(**kwargs)
    context['art'] = Art.objects.filter(project__in=projects, artist__visible=True).order_by('artist__name')
    return ''

@register.simple_tag(takes_context=True)
def project_artists(context, **kwargs):
    # try:
    #     art = project_art(**kwargs).distinct('artist__name')
    # except NotImplementedError:
    project_art(context, **kwargs)
    context['artists'] = sorted(set(art.artist for art in context['art'] if art.artist.visible), key=lambda x: x.name.split()[-1])
    return ''