from django import forms 

class PostForm (forms.Form):
    title=forms.CharField()
    text=forms.CharField(widget=forms.Textarea)
    is_enable=forms.BooleanField()
    publish_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
