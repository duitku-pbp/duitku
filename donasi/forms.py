from django import forms

class addNewDonasi(forms.Form):
    Nama = forms.CharField(label='Nama', required=True, max_length = 100)
    Nominal = forms.CharField(label='Nominal', required=True)
    Tujuan = forms.CharField(label='Tujuan', required=True)