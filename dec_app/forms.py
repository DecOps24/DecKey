from django import forms

from .models import Staff, Party, Work_Details


class DateInput(forms.DateInput):

    input_type = 'date'



class Staff_form(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'



class Party_form(forms.ModelForm):
    class Meta:
        model = Party
        fields = '__all__'

class WorkDetailsForm(forms.ModelForm):
    Finished_date = forms.DateField(widget=DateInput,required=False)
    Delivery_Date = forms.DateField(widget=DateInput,required=False)
    class Meta:
        model = Work_Details
        fields = ['Party_name','Nature_of_work', 'Details', 'Assigned_to', 'Status', 'Finished_date', 'Delivery_Date', 'Bill_Amount', 'Fee_amount', 'DOR']

    # Party_name = forms.ModelChoiceField(queryset=Party.objects.all(), widget=forms.Select(attrs={'class': 'autocomplete'}))



