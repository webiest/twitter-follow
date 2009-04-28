from django import forms

class input_form(forms.Form):
    follower = forms.CharField(max_length=50, required=True, error_messages={'required':'Follower Name is required'})
    following = forms.CharField(max_length=50, required=True, error_messages={'required':'Following Name is required'})
    
    
