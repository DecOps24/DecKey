
import django_filters
from django import forms
from django_filters import CharFilter

from .models import Work_Details


# class WorkFilter(django_filters.FilterSet):
#     # Assigned_to = CharFilter(label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
#     #     'placeholder': 'Search', 'class': 'form-control'}))
#
#     class Meta:
#         model = Work_Details
#         fields = ('Assigned_to','Party_name')



import django_filters
from django import forms
from .models import Work_Details, Party, Staff

class WorkFilter(django_filters.FilterSet):
    Assigned_to = django_filters.ModelChoiceFilter(
        queryset=Staff.objects.all(),
        label="Assigned To",
        widget=forms.Select(attrs={
            'class': 'form-control',  # Add Bootstrap styling
        })
    )
    Party_name = django_filters.ModelChoiceFilter(
        queryset=Party.objects.all(),
        label="Party Name",
        widget=forms.Select(attrs={
            'class': 'form-control',  # Add Bootstrap styling
        })
    )

    class Meta:
        model = Work_Details
        fields = ['Assigned_to', 'Party_name']
