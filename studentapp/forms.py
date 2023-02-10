
from django.contrib.auth.forms import UserCreationForm
from django import forms


from studentapp.models import Login, addmarks


class DateInput(forms.DateInput):
    input_type='date'


class studentform(UserCreationForm):
   DOB = forms.DateField(widget=DateInput)
   photo = forms.ImageField()
   def clean_photo(self):
       photo=self.cleaned_data.get('photo')
       if photo:
           if photo.size<=1 * 1024 + 1024 :
               raise forms.ValidationError('image size should not be greater than 1 MB ')
       return photo

   class Meta:
        model=Login
        fields=('username','password1','password2','name','phonenumber','DOB','photo',)



# class studentform(forms.ModelForm):
#     DOB = forms.DateField(widget=DateInput)
#     # image = forms.ImageField(min_size=100k)
#     class Meta:
#         model=studentregister
#         exclude = ('user','marks',)

class markform(forms.ModelForm):
    class Meta:
        model=addmarks
        fields=('__all__')




