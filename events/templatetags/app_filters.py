from django import template
from events.models import EventsChallenges,Events
from challenges.models import Challenges

register = template.Library()

@register.filter(name='used_by')
def used_by(chall_id,event_id):
    return EventsChallenges.objects.filter(challenge=Challenges.objects.get(id=chall_id.id),event=Events.objects.get(id=event_id.id)).count()

@register.filter(name='isUsed')
def isUsed(chall_id):
    return EventsChallenges.objects.filter(challenge=Challenges.objects.get(id=chall_id.id))
