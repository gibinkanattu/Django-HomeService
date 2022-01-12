from django import forms
from django.contrib.auth.models import User
from HSSapp.models import Profile, Location, RequestWork, Order, Chat


class registerform(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }


class loginform(forms.ModelForm):
    class Meta():
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['username', 'password']

        # def clean(self):
        #
        #     name = self.cleaned_data.get('username')
        #     pwd = self.cleaned_data.get('password')
        #     user = User.objects.get(username=name)
        #     flag = 0
        #     print('clean data')
        #     l1 = len(user)
        #     if l1 == 1:
        #         if user.password == pwd:
        #             flag = 1
        #     else:
        #         msg2 = "invalid username"
        #         self.add_error('username', msg2)
        #     if flag == 0:
        #         msg2 = "invalid password"
        #         self.add_error('password', msg2)


class locationform(forms.ModelForm):
    place = forms.CharField(required=False)

    class Meta():
        model = Location
        fields = ['state', 'district', 'area', 'place']


class profileform(forms.ModelForm):
    class Meta():
        model = Profile
        widgets = {
            'phone': forms.NumberInput()
        }
        fields = ['phone', 'job']


class phoneform(forms.ModelForm):
    class Meta():
        model = Profile
        widgets = {
            'phone': forms.NumberInput()
        }
        fields = ['phone']


class jobform(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['job']


class searchform(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['job']


class workform(forms.ModelForm):
    class Meta():
        model = RequestWork
        fields = ['notice', 'category']
        widgets = {'notice': forms.Textarea(
            attrs={'rows': 1, 'cols': 30, 'placeholder': 'Enter the message to send to workers'})}


class Chatform(forms.ModelForm):
    class Meta():
        model = Chat
        fields = ['message']
