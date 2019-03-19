from django import forms
from .models import StudentInfo


class StudentInfoForm(forms.ModelForm):

    class Meta:
        model = StudentInfo
        fields = [
            'name',
            'dept',
            'email',
            'phone'
        ]