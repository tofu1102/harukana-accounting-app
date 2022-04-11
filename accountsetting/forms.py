from django import forms

from accounts.models import CustomUser

class CustomUserSettingForm(forms.Form):
    username = forms.CharField(max_length = 150)
    def __init__(self, CustomUser, *args, **kwargs):
        super(CustomUserSettingForm,self).__init__(*args,**kwargs)
        if CustomUser :
            self.fields['username'].initial = CustomUser.username

class searchCustomUserForm(forms.Form):
    id = forms.CharField()
