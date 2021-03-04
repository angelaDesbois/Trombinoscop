from django import forms #on importe biblitheque forms
from trombi.models import Person, Student, Employee

class LoginForm(forms.Form): #heritage de la classe forms.Form de django
    email= forms.EmailField(label='Email')
    password = forms.CharField(label='Mot de passe', widget = forms.PasswordInput)

    def clean(self):
        cleaned_data =super (LoginForm, self).clean()#appel de la fonction de la classe parente (av super)
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            result = Person.objects.filter(password=password, email=email)
            if len(result) !=1:
                raise forms.ValidationError("Adresse de mail ou mot de passe erroné.")#methode python
        return cleaned_data


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ('friends',)

class EmployeeProfileForm(forms.ModelForm):
    class Meta: 
        model= Employee
        exclude = ('friends',)

class AddFriendForm(forms.Form):
    email = forms.EmailField(label='email :')
    def clean(self):
        cleaned_data = super(AddFriendForm, self).clean()
        email = cleaned_data.get("email")

        if email:
            result = Person.objects.filter(email= email)
            if len(result) != 1:
                raise forms.ValidationError("Adresse d' email erronée")
        return cleaned_data