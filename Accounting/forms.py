from django import forms

from .models import *
from accounts.models import CustomUser as member

class addPayForm(forms.Form):
    payer = forms.ModelChoiceField(label='payer',queryset=member.objects.none())
    payee = forms.MultipleChoiceField(label='payee',choices=(1,1))
    price = forms.CharField(label='price')
    purpose = forms.CharField(max_length = 50,required = False)
    def __init__(self, event, *args, **kwargs):
        super(addPayForm,self).__init__(*args,**kwargs)
        if event :
            self.fields['payer'].queryset = event.Member.all()
            self.fields['payee'].choices = [(i.username,i.username) for i in event.Member.all()]

class searchHistoryForm(forms.Form):
    payer = forms.ModelChoiceField(label='payer',queryset=member.objects.none(),required = False)
    payee = forms.MultipleChoiceField(label='payee',choices=(1,1),required = False)
    def __init__(self, event, *args, **kwargs):
        super(searchHistoryForm,self).__init__(*args,**kwargs)
        if event :
            self.fields['payer'].queryset = event.Member.all()
            self.fields['payee'].choices = [(i.username,i.username) for i in event.Member.all()]

class createEventForm(forms.Form):
    member = forms.MultipleChoiceField(label='members',choices=(1,1))
    name = forms.CharField(label='Event Name')
    def __init__(self, member, *args, **kwargs):
        super(createEventForm,self).__init__(*args,**kwargs)

        self.fields['member'].choices = [(i.username,i.username) for i in member.friend.filter(is_active = True) if i.username != "admin"] +[(member.username,member.username)]
