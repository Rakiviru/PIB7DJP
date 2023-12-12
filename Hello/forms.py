from django import forms

# class studentform(forms.Form):
#     students_ID = forms.IntegerField()
#     students_name = forms.CharField()
#     course = forms.CharField()
#     jdate = forms.DateField()

# creating forms using models
from django.forms import ModelForm
from Hello.models import students
class studentform(ModelForm):
    class Meta:
        model=students
        # fields = 'all'
        fields = ['student_ID', 'student_name', 'course', 'jdate']


# creating a form to add an student
form = studentform()
