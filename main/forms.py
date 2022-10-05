from django import forms
from .models import Technology, Project


class TechnologyForm(forms.ModelForm):

    class Meta:
        model = Technology
        fields = "__all__"


class ProjectForm(forms.ModelForm):
    stack = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Technology.objects.all(), required=False)

    class Meta:
        model = Project
        fields = "__all__"

