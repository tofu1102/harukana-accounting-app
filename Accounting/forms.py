from django import forms

from .models import *

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
