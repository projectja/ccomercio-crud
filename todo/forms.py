from django import forms
from .models import Tarea, Projects


class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = ['tarea']

class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Projects
        fields = ['company','description','program','generated_deca']


