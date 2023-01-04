from django import forms
from . models import Contact
from django.forms import TextInput , ModelForm , EmailInput , Textarea

class ContactForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control border-top-0 border-right-0 border-left-0 p-0', 'placeholder':'Your Name'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={ 'class':'form-control border-top-0 border-right-0 border-left-0 p-0', 'placeholder':'Your E-mail'}))
    # subject = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-control border-top-0 border-right-0 border-left-0 p-0', 'placeholder':'Subject'}))
    # messeage = forms.CharField(widget=forms.Textarea(attrs={ 'class':'form-control border-top-0 border-right-0 border-left-0 p-0' , 'placeholder':'Your Message'}))

    class Meta:
        model = Contact
        fields = ['name' , 'email' , 'subject' , 'message' ]
        widgets = {
            'name' : TextInput(attrs={'class':'form-control border-top-0 border-right-0 border-left-0 p-0', 'placeholder':'Your Name'}),       
            'email' : EmailInput(attrs={'class':'form-control border-top-0 border-right-0 border-left-0 p-0', 'placeholder':'Your E-mail'}),
            'subject' : TextInput(attrs={'class':'form-control border-top-0 border-right-0 border-left-0 p-0', 'placeholder':'Enter Your Subject'}),
            'message' : Textarea(attrs={'class':'form-control border-top-0 border-right-0 border-left-0 p-0', 'placeholder':'Please explain Your Problem'}), 
            
            }
    
    # def save(self):
    #     pass