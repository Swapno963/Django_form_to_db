from django import forms 
from first_app.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields =  "__all__"
        # fields = ['name','address']
        # exclude = ['roll']
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll'
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class':'btn-primary'}),
            'roll': forms.PasswordInput()
        }

        help_texts = {
            'name' : 'Write Your Name'
        }

        error_messages = {
            'name' : {'requered':'Your name is requered'}        }