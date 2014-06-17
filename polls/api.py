# mysite/polls/api.py
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from polls.models import Poll, Choice
from tastypie import fields
from authentication import OAuth20Authentication
 
class ChoiceResource(ModelResource):
    class Meta:
        queryset = Choice.objects.all()
        resource_name = 'choice'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()
 
class PollResource(ModelResource):
    choices = fields.ToManyField(ChoiceResource, 'choice_set', full=True)
    class Meta:
        queryset = Poll.objects.all()
        resource_name = 'poll'
        authorization = DjangoAuthorization()
        authentication = OAuth20Authentication()