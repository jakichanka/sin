from django import forms

class Link(forms.Form):
    name = forms.CharField(max_length=30,label='Введите имя :',required=True)
    email = forms.EmailField(max_length=254,label='email :',required=True)
    message = forms.CharField(widget=forms.Textarea)


    def clean_massage(self):
        data = self.cleaned_data['massage']